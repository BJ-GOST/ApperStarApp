from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from accounts import urls
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail



#DOCUMENTATION FOR APPERSTAR BLOGGING APP
'''
This is the documentation of the part of this project that involves the creation 
and updating of the blog and may be extended in the future in accordance with 
the company needs. Above every function in this file is a phrase or detailed
expression of what the function does and in other cases; suggestions of how it
can be extended in the future. I would also advice for anyone who reviews the code
to leave clear documentations on whatever changes they may have made to the code
for purposes of clarity. 

REQUIREMENTS

1. Please skip ten lines after every function to enhance visibility.
2. Make sure the function name corresponds with the name of the 
template file it calls and the corresponding url used in accessing
the function.
3. Make sure to leave a detailed documentation every time you refactor
the base code.
4. In any case where you use any sort of rule to define your variables
please remember to clearly define the rules you used at the head of the 
function.
5. Give a phrase at the head of every function as a short description of 
the function.
6. Where possible define the context dictionary in a single line.

Happy Coding!
'''










#function for creating a blog
'''
The createblog function is used to create the blogs
and doesn't quite have much
It would do better to notify subscribed users
of any new blogs posted by the respective 
authors they're subscribed to
also the arguments in the redirect function
could be changed to the url concerned with
displaying the details of the blog along with
form_object.id. The form object in this function
is an instance of the form which is retrieved 
before commiting the changes to the database for passing values 
that can otherwise not be given by the user in this instance the 
user associated with a certain blog.

'''
@login_required(login_url='login')
def createblog(request):
    form = blogform()
    if request.method == 'POST':
        form = blogform(request.POST, request.FILES)
        if form.is_valid():
            form_object = form.save(commit=False)
            form_object.author = request.user
            blogger = form_object.author
            User = form_object.author
            form_object.save()
            return redirect('my-blogs', User.id)
    return render (request, 'createblog.html', {'form': form})










#function for creating a blog
'''
The update_blog function is used to access an instance of a blog 
for the purpose of updating. It still uses the blogform class 
imported from the .forms file but passes a blog instance as an argument
this in turn returns the instance of the blog to be updated. 

'''
@login_required(login_url='login')
def update_blog(request, pk):
    Blog = blog.objects.get(id=pk)
    form = blogform(instance=Blog)
    context = {'form': form}
    template_name = 'updateBlog.html'
    if request.method == 'POST':
        form = blogform(request.POST, instance=Blog)
        if form.is_valid():
            form.save()
            return redirect('blogdetail', Blog.id)
        else:
            form = blogform(instance=Blog)
    return render(request, template_name, context) 










#function for list of all blogs
'''
This function is responsible for displaying all blogs 
that have ever been posted. I recommend changing the 
function name to all_blogs and the name of the corresponding
template file to that

'''
def blogs(request):
    blogs = blog.objects.all()
    total = blogs.count()
    if total >= 1:
        display_blog = blog.objects.get(id=total)
    else:
        display_blog= None
    context = {'blogs': blogs, 'display_blog':display_blog}
    template_name = 'blogs.html'
    return render (request, template_name, context)










#function for listing all blog posts belonging to a given user
'''
This function calls all the blogs related to a particular user
I recommend changing its name to user_blogs and the  template name 
to that as well

'''
@login_required(login_url='login')
def my_blogs(request, pk):
    Blogs = blog.objects.filter(author_id=pk)
    context = {'Blogs': Blogs}
    template_name = 'myblogs.html'
    return render(request, template_name, context)
    









#function for a detailview of the blog and for commenting
'''
This function calls a detail view of the blog.
It also displays the comments related to a particular 
post. I recommend refactoring the subscritpion functionality
by first requiring a user to login before subscribing; this way
a user is automatically added to a subscription list
The form_object variable refers to the uncommitted instance of an 
object

'''
def blogdetail(request, pk):
    template_name = 'blogdetail.html'
    Blog = blog.objects.get(id=pk)
    my_comments =comment.objects.filter(blog_id=pk)
    new_comment = None
    form = commentform()

    if request.method == 'POST' and 'comment' in request.POST:
        form = commentform(data=request.POST)
        if form.is_valid():
            form_object = form.save(commit=False)
            form_object.blog = Blog
            form_object.author = request.user
            form_object.save()
            form = commentform()

    if request.method == 'POST' and 'subscribe' in request.POST:
        s_form = SubscriptionForm(request.POST)
        if s_form.is_valid():
            form_object = s_form.save(commit=False)
            form_object.blogger = Blog.author
            form_object.save()
            s_form = SubscriptionForm()

    else:
        form = commentform()
        s_form = SubscriptionForm()
    context={'Blog': Blog, 'my_comments': my_comments, 'new_comment': new_comment, 's_form': s_form, 'form': form}
    return render(request, template_name, context)










#function for comment detailview and replying
'''
This function returns a context dictionary which includes
a comment detail and replies related to that comment.
'''
@login_required(login_url='login')
def comment_detail(request, pk):
    template_name = 'comment.html'
    comment_detail = get_object_or_404(comment, id=pk)
    my_replies = reply.objects.filter(comment_id=pk)
    new_reply = None 

    if request.method == 'POST':
        form = replyform(data=request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.comment = comment_detail
            new_reply.author = request.user
            new_reply.save()
            form = commentform()
    else:
        form = commentform()
    context = {'comment_detail':comment_detail, 'my_replies': my_replies, 'new_reply': new_reply, 'form':form }
    return render(request, template_name, context)









#function for liking a blog
'''
This function works perfectly and I'd advice unless
you know what you're really upto; it's best left as it
is

'''
@login_required(login_url='login')
def like_blog(request):
    user = request.user
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        Blog = blog.objects.get(id=blog_id)

        if user in Blog.liked.all():
            Blog.liked.remove(user)
        else:
            Blog.liked.add(user)

        Like, created = like.objects.get_or_create(user=user, blog_id=blog_id)
        
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save(Blog)
    return redirect('blogdetail', blog_id)









#function for shoiwng a blogger to a list of subscribers
'''
This function does not seem to work appropriately
by returning a list of users. The subscribers queryset
defined instead seems to be returning a list of blogs.

'''
@login_required(login_url='login')
def subscribers(request, pk):
    subscribers = subscription.objects.filter(blogger_id=pk)
    template_name='subscribers.html'
    context = {'subscribers':subscribers}
    return render (request, template_name, context)


            





