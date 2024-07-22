from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .forms import UserRegisterForm, UploadForm, GardeningGroupForm
from .models import CommunityGarden, GardeningGroup, UserHistory, Upload, Post
from django.shortcuts import render, redirect, get_object_or_404
from .models import Upload, Post, Profile, GardeningGroup
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GroupPostForm,UserUpdateForm, ProfileForm, LoginForm
from django.http import HttpResponseForbidden
from django.contrib.auth.views import LoginView

def homes(request): #rosh
    if request.user.is_authenticated:
        image_posts = Upload.objects.filter(photo__isnull=False)
        text_posts = Upload.objects.filter(photo__isnull=False)
        return render(request, 'garden_app/homes_logged_in.html', {'image_posts': image_posts, 'text_posts': text_posts})
    else:
        uploads = Upload.objects.all()
        return render(request, 'garden_app/homes.html', {'uploads': uploads})
    
    
def register(request): #rosh
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homes')
    else:
        form = UserRegisterForm()
    return render(request, 'garden_app/register.html', {'form': form})


@login_required #rosh
def profile(request):
    user = request.user
    recent_posts = Post.objects.filter(author=user).order_by('-created_at')[:5]
    groups_joined = GardeningGroup.objects.filter(members=user)

    context = {
        'user': user,
        'recent_posts': recent_posts,
        'groups_joined': groups_joined,
    }
    return render(request, 'garden_app/profile.html', context)


@login_required #rosh
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            if upload.photo:
                return redirect('homes')
            else:
                # Handle redirection or saving logic for text-only posts
                return redirect('homes')
    else:
        form = UploadForm()
    return render(request, 'garden_app/upload.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = LoginForm