from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from . models import Blog
from .forms import edit_blog

from django.contrib import messages
# Create your views here.


def index(request):
    blog= Blog.objects.all()
    contex={'blogs':blog}
    return render(request,"home.html",contex)


def user_register(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            messages.warning(request,'password does not match')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'uname already taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already taken')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pass1)
            user.save()
            messages.success(request,'user register sucessfully')
            return redirect("login")

    return render(request,"register.html")

def user_login(request): 

    if request.method=="POST":
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'invalid creditial')
            return redirect("login")
    return render(request,"login.html")



def user_logout(request):
    
    logout(request)
    return redirect('/')

def post_blog(request):
    if request.method=="POST":
        title=request.POST.get('title')
        descr=request.POST.get('desc')
        blog = Blog(title=title,disc=descr,user_id=request.user)
        blog.save()
        messages.success(request,'Sucessfully  created')
        return redirect("post_blog")
        
    return render(request,'blog_post.html')


def blog_detail(request,id):
    blog= Blog.objects.get(id=id)
    context={'blog':blog} 
    return render(request,'blog_detail.html',context) 

def blog_delete(request,id):
     blog= Blog.objects.get(id=id)
     blog.delete()
     messages.success(request,'Blog deleted sucessfully')
     return redirect('/')


def edit(request,id):
    blog= Blog.objects.get(id=id)
    edit_b=edit_blog(instance=blog)
    if request.method=="POST":
        form=edit_blog(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,"post has been updated")
            return redirect('/')
    return render(request,'edit_blog.html',{'edit_blo':edit_b})

