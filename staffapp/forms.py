from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
class registeration(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name']

class Userform(forms.ModelForm):
    class Meta:
         model=User
         fields=['username','first_name','last_name']

class Profileform(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields=['phone_number','email','website','department','postion']
