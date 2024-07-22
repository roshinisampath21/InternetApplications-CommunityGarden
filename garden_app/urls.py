from django.urls import path
from . import views
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
    path('groups/<int:group_id>/leave/', views.leave_group, name='leave_group'),]