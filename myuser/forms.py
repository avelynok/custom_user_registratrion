from django import forms
from django.contrib.auth.forms import UserCreationForm
from myuser.models import MyUser

class SignupForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 
                  'displayname'
                )
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)