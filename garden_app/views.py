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


@login_required #yash
def delete_upload(request, upload_id):
    upload = get_object_or_404(Upload, id=upload_id)
    if upload.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    if request.method == 'POST':
        upload.delete()
        return redirect('homes')
    return render(request, 'garden_app/delete_upload.html', {'upload': upload})


@login_required
def add_post(request, group_id): #yash
    group = get_object_or_404(GardeningGroup, id=group_id)
    if request.user not in group.members.all():
        return HttpResponseForbidden("You are not allowed to post in this group.")

    if request.method == 'POST':
        form = GroupPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.group = group
            post.author = request.user
            post.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupPostForm()

    return render(request, 'garden_app/add_post.html', {'form': form, 'group': group})


@login_required #yash
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    if request.method == 'POST':
        post.delete()
        return redirect('group_detail', group_id=post.group.id)
    return render(request, 'garden_app/delete_post.html', {'post': post})


@login_required #yash
def user_history(request):
    total_visits = request.session.get('total_visits', 0)
    daily_visits = request.session.get('daily_visits', {})
    return render(request, 'garden_app/user_history.html', {
        'total_visits': total_visits,
        'daily_visits': daily_visits
    })

@login_required
def join_group(request, group_id):  #rehaan
    group = get_object_or_404(GardeningGroup, id=group_id)
    group.members.add(request.user)
    return redirect('group_detail', group_id=group_id)

@login_required
def leave_group(request, group_id):  #rehaan
    group = get_object_or_404(GardeningGroup, id=group_id)
    group.members.remove(request.user)
    return redirect('group_detail', group_id=group_id)

@login_required
def group_about(request, group_id):  #rehaan
    group = get_object_or_404(GardeningGroup, id=group_id)
    return render(request, 'garden_app/group_about.html', {'group': group})


def edit_profile(request):  #rehaan
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'garden_app/edit_profile.html', {'form': form})
