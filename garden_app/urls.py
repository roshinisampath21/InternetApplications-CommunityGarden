from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homes, name='homes'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete/<int:upload_id>/', views.delete_upload, name='delete_upload'),
    path('groups/', views.groups_list, name='groups_list'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('groups/<int:group_id>/join/', views.join_group, name='join_group'),
    path('groups/<int:group_id>/leave/', views.leave_group, name='leave_group'),
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('create_group', views.create_group, name='create_group'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('group/<int:group_id>/about/', views.group_about, name='group_about'),
    path('groups/<int:group_id>/add_post/', views.add_post, name='add_post'),
    path('groups/post/<int:post_id>/delete/', views.delete_post, name='delete_post'),  # Adjusted line
    path('groups/<int:group_id>/delete/', views.delete_group, name='delete_group'),
    path('user_history/', views.user_history, name='user_history'), 
    ]