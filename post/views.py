from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

# Create your views here.


@login_required(login_url="login")
def PostFeed(request):
    post = Post.objects.all().order_by('-id')
    context = {"post": post}
    return render(request, "post/postfeed.html", context)


@login_required(login_url="login")
def CreatePost(request):
    # postform = PostForm()
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            postform.save(commit=False).user = request.user
            postform.save()
        return redirect("index")
    # context = {'form': postform}
    return render(request, "post/createpost.html")


@login_required(login_url="login")
def UpdatePost(request, pk):
    post = Post.objects.get(rndid=pk)
    postform = PostForm(instance=post)

    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save(commit=False).user = request.user
            postform.save()
            return redirect('index')
    return render(request, 'post/update.html', {'form': postform})


@login_required(login_url="login")
def DeletePost(request, pk):
    post = Post.objects.get(rndid=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'post/delete.html', {'post': post})


def Login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            user = request.POST.get("username")
            passw = request.POST.get("password")
            user = authenticate(request, username=user, password=passw)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.info(request, "Username or Password is Incorrect")

    return render(request, "post/login.html")


def Register(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account Created For " + user)
                return redirect("login")

    context = {"register": form}
    return render(request, "post/register.html", context)


def Logout(request):
    logout(request)
    return redirect("login")
