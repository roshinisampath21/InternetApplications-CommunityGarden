from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Upload
from .models import GardeningGroup
from .models import Post
from .models import Profile

class UserRegisterForm(UserCreationForm): #rosh
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm): #rosh
    class Meta:
        model = User
        fields = ['username', 'email']