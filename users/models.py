from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#class UserRegisterForm(UserCreationForm):
 #   email = forms.EmailField()

  #  class Meta:
   #     model = User
    #    fields = ['username', 'email', 'password1', 'password2']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)



