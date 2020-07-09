from django.shortcuts import HttpResponse, render, redirect
from django.core.mail import send_mail
from .models import Contact, Register, Project, Blogs, BlogComment
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


def index(request):
    projects = (Project.objects.all())
    if request.method == "POST":
        message_name = "Thankyou for joining us :)"
        email = request.POST['email']
        if not Register.objects.filter(email=email):
            register = Register(email=email)
            register.save()
            msg = 'You are now connected to out network.'
            params = {'email': email, 'msg': msg, 'projects': projects}
            return render(request, 'web/index.html', params)
        else:
            params = {'email': "You are already registered with Us", 'projects': projects}
            return render(request, 'web/index.html', params)
    else:
        params = {'projects': projects}
        return render(request, 'web/index.html', params)


def about(request):
    return render(request, 'web/about.html')


def bloghome(request):
    blogs = Blogs.objects.all()
    latestPosts = Blogs.objects.all().order_by('-p_id')[0:6]
    if request.method == "POST":
        email = request.POST.get('emailblog')
        if not Register.objects.filter(email=email):
            register = Register(email=email)
            register.save()
            msg = 'You are now connected to our network.'
            messages.success(request, "Yippee ! We are now connected")
            params = {'emailblog': email, 'msg': msg, 'blogs': blogs, 'latestPosts': latestPosts}
        else:
            msg = 'You are already connected to our network.'
            messages.success(request, "Hey , We are already connected.")
            params = {'blogs': blogs, 'latestPosts': latestPosts, 'msg': msg}
        return render(request, 'web/blog.html', params)
    else:
        params = {'blogs': blogs, 'latestPosts': latestPosts}
        return render(request, 'web/blog.html', params)


def contact(request):
    mapbox_access_token = 'pk.eyJ1IjoiYW1hbm52bCIsImEiOiJja2M5ZmN6bXExNG40MzJueGY5NTR2eXo1In0.oZf_CZfJUVV9Nw-Pm7ogGA'
    params = {'mapbox_access_token': mapbox_access_token}
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']
        message_subject = request.POST['subject']
        if len(message_name) < 4 or len(message_email) < 8 or len(message_subject) < 4 or len(message) < 10:
            messages.error(request, "Please fill the details correctly.")
        else:
            contact = Contact(name=message_name, email=message_email, subject=message_subject, message=message)
            contact.save()
            send_mail(
                message_subject,  # subject
                message,  # message
                message_email,  # from email
                ['amannvl3@gmail.com'],  # to email
            )
            messages.success(request, "Your request has been sent")
            params = {'message_name': message_name, 'mapbox_access_token': mapbox_access_token}
        return render(request, 'web/contact.html', params)
    else:
        params = {'mapbox_access_token': mapbox_access_token}
        return render(request, 'web/contact.html', params)


def portfolio(request):
    projects = (Project.objects.all())
    params = {'projects': projects}
    return render(request, 'web/portfolio.html', params)


def elements(request):
    return render(request, 'web/elements.html')


def portfoliodetails(request, p_id):
    post = Project.objects.filter(p_id=p_id).first()
    context = {'post': post}
    return render(request, 'web/portfolio-details.html', context)


def services(request):
    return render(request, 'web/services.html')


def singleblog(request, title):
    blogdata = Blogs.objects.filter(title=title).first()
    latestPosts = Blogs.objects.all().order_by('-p_id')[0:3]
    comments = BlogComment.objects.filter(blog=blogdata)
    # email = request.POST['emailblog']
    if request.method == "POST":
        email = request.POST.get('emailblog')
        if not Register.objects.filter(email=email):
            register = Register(email=email)
            register.save()
            msg = 'You are now connected to our network.'
            params = {'emailblog': email, 'msg': msg, 'blogdata': blogdata, 'latestPosts': latestPosts,
                      'comments': comments, 'user': request.user}
        else:
            msg = 'You are already connected to our network.'
            params = {'blogdata': blogdata, 'latestPosts': latestPosts, 'msg': msg, 'comments': comments}
        return render(request, 'web/single-blog.html', params)
    else:
        params = {'blogdata': blogdata, 'latestPosts': latestPosts, 'comments': comments}
        return render(request, 'web/single-blog.html', params)


def blogwrite(request):
    if request.method == "POST":
        title = request.POST['title']
        user = request.user
        subtitle = request.POST['subtitle']
        specialmsg = request.POST['specialmsg']
        desc = request.POST['desc']
        referral_url = request.POST['referral_url']
        category = request.POST['category']
        date = request.POST['date']
        keyword = request.POST['keyword']
        if len(title) < 4:
            messages.error(request, "Fill the details correctly")
        else:
            newblog = Blogs(title=title, user=user, subtitle=subtitle, specialmsg=specialmsg, desc=desc,
                           referral_url=referral_url, category=category, date=date, keyword=keyword)
            newblog.save()
            messages.success(request, "Congratulations ! Your blog has been posted successfully.")
    return render(request, 'web/blogwrite.html')


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        blogp_id = request.POST.get("blogp_id")
        blog = Blogs.objects.get(p_id=blogp_id)
        # parent =
        comment = BlogComment(comment=comment, user=user, blog=blog)
        comment.save()
        messages.success(request, "Your comments has been posted successfully")
        comments = BlogComment.objects.filter(blog=blog)
        params = {'blogdata': blog, 'comments': comments}
    return render(request, 'web/single-blog.html', params)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checks
        if len(username) > 10:
            messages.error(request, "Username cannot exceed 10 characers.")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers.")
            return redirect('signup')
        if pass1 != pass2:
            messages.error(request, "Password do not match.")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return render(request, 'web/signup.html')

    else:
        # messages.error("Sorry ! Account cannot be created at the moment.")
        return render(request, 'web/signup.html')


def login(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials ! Please try again")
            return redirect('login')

    return render(request, 'web/login.html')


def logout(request):
    # if request.method == 'POST':
    auth_logout(request)
    messages.success(request, "Successfully logged Out.")

    return redirect('home')
