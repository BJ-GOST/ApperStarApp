
from .forms import CreateProfile, UpdateProfile
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from verify_email.email_handler import send_verification_email
from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


User = get_user_model()
# Create your views here.
def landing(request):
	return render(request, 'landing.html')


@login_required(login_url='login')
def apper(request):
	return render(request, 'apper.html')



def register(request):
	form = CreateProfile()
	template_name = 'CreateProfile.html'
	context = {'form':form}
	if request.method == 'POST':
		form = CreateProfile(request.POST)
		if form.is_valid():
			inactive_user = send_verification_email(request, form)
			#form.save()
			return redirect('waiting')
	return render (request, template_name, context)


def waiting(request):
	template_name = 'waiting.html'
	return render (request, template_name)




def login(request):
	template_name = 'login.html'
	if request.user.is_authenticated:
		return redirect('landing')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('blogs')
		else:
			messages.error(request, 'please check your password or username')
	return render (request, template_name)





@login_required(login_url='login')
def logout(request):
	template_name = 'landing.html'
	auth.logout(request)
	return render(request, template_name)





def UpdateProfile(request):
	context = {}
	template_name = 'updateprofile.html'
	return render (request, template_name, context)




def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'apperstarStudios@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})