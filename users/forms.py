from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProfileForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    phone_number = forms.CharField()
    education_level = forms.CharField()
    educational_institutions = forms.CharField()
    work_experience = forms.CharField()
    skills = forms.CharField()

