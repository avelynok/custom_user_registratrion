from django.shortcuts import render, reverse, HttpResponseRedirect
from myuser.models import MyUser
from myuser.forms import LoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from customuser import settings

# Create your views here.
def home(request):
    data = MyUser.objects.all()
    return render(request, 'home.html')

@login_required
def index(request):
    data = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'data': data})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data['username'],
                displayname=data['displayname'],
                password=data['password1'],
            )
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'SignupForm.html', {'form': form})

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate( 
                request, 
                username = data['username'], 
                password = data['password']
                )
            if user:
                login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next' , reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'LoginForm.html', {'form': form})

def logoutview(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return HttpResponseRedirect(reverse('home'))