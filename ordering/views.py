from django.shortcuts import render, redirect
from .forms import *
import datetime
from django.contrib.auth.decorators import login_required
from django_daraja.mpesa.core import MpesaClient
from django.urls import reverse
from django.http import HttpResponse



#from here the user can see his/her previously created jobs
#the link to the order type selection is also found here
@login_required(login_url='login')
def jobs_page(request, pk):
	jobs = Job.objects.filter(user_id=pk)
	count = jobs.count()
	context = {'jobs': jobs, 'count':count}
	template_name = 'jobs_page.html'
	return render(request, template_name, context)


#returns a detailed view of each job
@login_required(login_url='login')
def job_detail(request, pk):
	job = Job.objects.get(id=pk)
	schedules = Schedule.objects.filter(job_id=pk)
	schedules_true = schedules.filter(completed=True)
	schedules_false = schedules.filter(completed=False)
	complete_modules = schedules_true.count()
	incomplete_modules = schedules_false.count()
	Total = incomplete_modules + complete_modules
	if Total == 0:
		progress = 0
	else:
		print(Total, incomplete_modules, complete_modules)
		calc = (complete_modules/Total) * 100
		progress= round(calc, 1)
	context = {'job':job, 'schedules_true':schedules_true, 'schedules_false':schedules_false, 'progress':progress, 'schedules':schedules, 'Total':Total}
	template_name = 'job_detail.html'
	return render(request, template_name, context)


#this is the view used for searching for jobs on the jobs page
@login_required(login_url='login')
def search(request):
	template_name='jobs_page.html'
	if request.method == 'POST':
		title = request.POST.get('title')
		jobs = Job.objects.filter(title=title)
		context = {'jobs':jobs}
		return render(request, template_name, context)


#here the user can select whether to make a custom order or a guided order
@login_required(login_url='login')
def job_select(request):
	template_name = 'job_select.html'
	return render(request, template_name)




#this is for the custom orders page
@login_required(login_url='login')
def custom_job(request):
	form = CustomJobForm()
	template_name = 'custom_job.html'
	context = {'form':form}

	if request.method == 'POST':
		form = CustomJobForm(request.POST)
		if form.is_valid():
			cust_form = form.save(commit=False)
			cust_form.user = request.user 
			category = form.cleaned_data.get('category')
			cust_form.save()
			body = f'{request.user} posted a new job'
			notification=Notification(user=cust_form.user, category=category, job=cust_form, body=body, timestamp=datetime.datetime.now())
			notification.save()
			return redirect('job-detail', cust_form.id)
	return render(request, template_name, context)




#this is for the guided order pages and displays a list of possible options to choose from
@login_required(login_url='login')
def guided_job(request):
	template_name = 'guided_job_select.html'
	return render(request, template_name)



#for the graphic design page and form
@login_required(login_url='login')
def graphics(request):
	form = GraphicsDesignForm()
	template_name = 'graphics_des.html'
	context = {'form':form}
	if request.method == 'POST':
		form = GraphicsDesignForm(request.POST)
		if form.is_valid():
			graphics_form = form.save(commit=False)
			graphics_form.user = request.user
			graphics_form.category = 'Graphics Design'
			graphics_form.save()
			body = f'{request.user} posted a new job'
			notification = Notification(user=graphics_form.user, category='Graphics Design', job=graphics_form, body=body, timestamp=datetime.datetime.now())
			notification.save()
			return redirect('job-detail', graphics_form.id)
	return render(request, template_name, context)




#for the web dev page and form
@login_required(login_url='login')
def webdev(request):
	form = WebDevForm()
	template_name = 'webdev.html'
	context = {'form':form}
	if request.method == 'POST':
		form = WebDevForm(request.POST)
		if form.is_valid():
			webdev_form = form.save(commit=False)
			webdev_form.user = request.user
			webdev_form.category = 'Web Development'
			webdev_form.save()
			body = f'{request.user} posted a new job'
			notification = Notification(user=webdev_form.user, category='Web Development',job=webdev_form, body=body, timestamp=datetime.datetime.now())
			notification.save()
		return redirect('job-detail', webdev_form.id)
	return render(request, template_name, context)




#for the info_systems page and form
@login_required(login_url='login')
def info_systems(request):
	form = InformationSystemsDesign()
	template_name = 'info_sys.html'
	context = {'form':form}
	if request.method == 'POST':
		form = InformationSystemDesign(request.POST)
		if form.is_valid():
			info_form = form.save(commit=False)
			info_form.user = request.user
			info_form.category = 'Information System Development'
			info_form.save()
			body = f'{request.user} posted a new job'
			notification = Notification(user=info_form.user, category='Information System Development',job=info_form, body=body, timestamp=datetime.datetime.now())
			notification.save()
			return redirect('job-detail', info_form.id)
	return render(request, template_name, context)




#for the mobile app dev page and form
@login_required(login_url='login')
def appdev(request):
	form = MobileAppDev()
	template_name = 'appdev.html'
	context = {'form':form}
	if request.method == 'POST':
		form = GuidedJobForm(request.POST)
		if form.is_valid():
			appdev_form = form.save(commit=False)
			appdev_form.user = request.user
			appdev_form.category = 'Mobile App Development'
			appdev_form.save()
			body = f'{request.user} posted a new job'
			notification = Notification(user=appdev_form.user, category='Mobile App Development',job=appdev_form, body=body, timestamp=datetime.datetime.now())
			notification.save()
			return redirect('job-detail', appdev_form.id)
	return render(request, template_name, context)




#this is the view for displaying all the notifications
#later you will create a view to display the viewed notification from the unviewed
@login_required(login_url='login')
def all_notifications(request):
	new_notifications = Notification.objects.filter(viewed=False)
	old_notifications = Notification.objects.filter(viewed=True)
	context = {
	'new_notifications': new_notifications,
	'old_notifications': old_notifications
	}
	template_name = 'all_notifications.html'
	return render(request, template_name, context)



#function to redirect the user and set the value of the notifcation_viewed to true
@login_required(login_url='login')
def notification_detail(request, pk):
	notification = Notification.objects.get(id=pk)
	context = {'notification':notification}
	template_name = 'notification_detail.html'
	if notification.viewed == False:
		notification.viewed = True
		notification.save()
	return render(request, template_name, context )



#a view to either deny or accept a job
@login_required(login_url='login')
def accept(request):
	template_name = 'success.html'
	if request.method == 'POST':
		notification_id=request.POST.get('notification_id')
		notification = Notification.objects.get(id=notification_id)
		notification.job.accepted = True 
		notification.job.apper = request.user
		notification.job.save()
		body = 'Your request has been accepted'
		message = Message(user=notification.user, notification=notification, body=body, timestamp=datetime.datetime.now())
		message.save()
	return render(request, template_name)



#a view to deny a job and send back the notification to the user
@login_required(login_url='login')
def deny(request):
	template_name = 'success.html'
	if request.method == 'POST':
		notification_id=request.POST.get('notification_id')
		notification = Notification.objects.get(id=notification_id)
		if notification.job.accepted == True:
			notification.job.accepted = False
			notification.job.save()
		else:
			notification.job.accepted = False
			notification.job.save()
		body = 'Your request has been denied'
		message = Message(user=notification.user, notification=notification, body=body, timestamp=datetime.datetime.now())
		message.save()
	return render(request, template_name)



#a view for the accepted jobs
@login_required(login_url='login')
def accepted_jobs(request, pk):
	jobs = Job.objects.filter(apper_id=pk)
	template_name = 'accepted.html'
	context ={'jobs': jobs}
	return render(request, template_name, context)



#this is a view rendering the notifications for any given single user
@login_required(login_url='login')
def my_notifications(request, pk):
	messages = Message.objects.filter(user_id=pk)
	viewed_messages = messages.filter(viewed=True)
	unviewed_messages = messages.filter(viewed=False)
	context={'messages': messages, 'viewed_messages':viewed_messages, 'unviewed_messages':unviewed_messages}
	template_name = 'my_notifications.html'
	return render(request, template_name, context)



#the scheduling functionality
'''
what we need for this
1. a view func for the scheduling itself
2. a view func where the user can see the scheduled job, modules and progress
3. a view func that shows all the jobs - use the accepted jobs view
4. the all jobs page should have filters- i opt for more than one filters
5. we may need a seperate function to handle all the scheduling and stuff
6. we need a form for creating the schedules/modules
7. a view url to mark a module as completed
8. place the button for completing a given module on the page sheduled jobs(yet to be created)
'''


#This is a view that aids in creating modules for a job(scheduling a job)
#this view handles both the job details and the scheduling
@login_required(login_url='login')
def job_scheduling(request, pk):
	template_name = 'scheduling.html'
	job = Job.objects.get(id=pk)
	modules = Schedule.objects.filter(job_id=pk)
	form = ScheduleForm()
	context = {'job':job, 'modules':modules,'form':form}
	if request.method == 'POST':
		form = ScheduleForm(request.POST)
		if form.is_valid():
			schedule_form = form.save(commit=False)
			schedule_form.job = job 
			schedule_form.save()
	return render(request, template_name, context)



#this view sets the scheduled attribute of a job to true
@login_required(login_url='login')
def schedule(request):
	template_name = 'success.html'
	if request.method == 'POST':
		job_id=request.POST.get('job_id')
		job = Job.objects.get(id=job_id)
		job.scheduled = True
		job.save()
	return render(request, template_name)



#this view returns a list of all scheduled jobs and from here users can mark modules as completed and track progress
@login_required(login_url='login')
def scheduled_jobs(request, pk):
	jobs = Job.objects.filter(apper_id=pk)
	scheduled_jobs = jobs.filter(scheduled=True)
	template_name = 'scheduled_jobs.html'
	context = {'scheduled_jobs':scheduled_jobs}
	return render(request, template_name, context)



#this view helps to update the already completed modules through button clicks
@login_required(login_url='login')
def scheduled_job_detail(request, pk):
	job = Job.objects.get(id=pk)
	modules = Schedule.objects.filter(job_id=pk)
	complete_modules = modules.filter(completed=True)
	incomplete_modules = modules.filter(completed=False)
	complete = complete_modules.count()
	incomplete = incomplete_modules.count()
	total= complete+incomplete
	calc= (complete)/total * 100
	percentage_completed = round(calc, 1)
	template_name = 'scheduled_job_detail.html'
	context = {'job':job, 'incomplete_modules':incomplete_modules, 'complete_modules':complete_modules, 'percentage_completed': percentage_completed}
	return render (request, template_name, context)


#this is a view to mark a module as completed
@login_required(login_url='login')
def complete(request):
	template_name = 'success.html'
	if request.method == 'POST':
		schedule_id=request.POST.get('schedule_id')
		schedule = Schedule.objects.get(id=schedule_id)
		schedule.completed = True
		schedule.save()
	return render(request, template_name)


#this is a view to control the viewed and unviewed user notifications
@login_required(login_url='login')
def viewed(request):
	template_name = 'message_detail.html'
	if request.method == 'POST':
		message_id = request.POST.get('message_id')
		message = Message.objects.get(id=message_id)
		job_title = message.notification.job.title
		job_date = message.notification.job.timestamp
		job_user = message.notification.job.user
		if message.viewed == False:
			message.viewed = True
		else:
			pass 
		message.save()
		context={'message':message, 'job_title':job_title, 'job_date':job_date, 'job_user':job_user}
	return render(request, template_name, context)



#mpesa payment
def payment_form(request):
	template_name = 'payment.html'
	return render(request, template_name)


# request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
def payment(request):
	cl = MpesaClient()
	template_name = 'paySuccess.html'
	if request.method == 'POST':
		phone_number = request.POST.get('phone')
		amount = int(request.POST.get('amount'))
		account_reference = 'ABC001'
		transaction_desc = 'Job payment'
		callback_url = 'https://darajambili.herokuapp.com/'
		response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
		return render(request, template_name)


def stk_push_callback(request):
        data = request.body
        return(data)


#this view will provide the user with information as we wait for the Mpesa API
def easy_pay(request):
	template_name = 'easy_pay.html'
	return render(request, template_name)

