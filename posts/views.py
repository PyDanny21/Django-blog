from django.shortcuts import render,redirect
from .models import Post,Profile
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
app_name='app'
def index(request):
    posts=Post.objects.all()
    paginator=Paginator(posts,1)
    page=request.GET.get('page')
    
    page_object=Paginator.get_page(paginator,page)
    return render(request,'post/index.html',{'posts':posts,'page_object':page_object})

def post(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,'post/page.html',{
        'post':post,
    })

def signup(request):
    if request.method== 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()

                #Log user in and redirect to settings page
                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                #create profile object for the new user
                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,user_id=user_model.id)
                new_profile.save()
                return redirect('login')
        else:
            messages.info(request,'Password not matching!')
            return redirect('signup')
    else:
        return render(request,'post/signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'post/login.html')
    
@login_required(login_url='login') 
def logout(request):
    auth.logout(request)
    return redirect('login')


    