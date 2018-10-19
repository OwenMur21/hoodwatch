from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighbour

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class CreateHoodForm(forms.ModelForm):
    """
    Model form class to create a neighbourhood
    """
    class Meta:
        model = Neighbour
        exclude =['user'] 
