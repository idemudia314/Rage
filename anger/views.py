from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
# Create your views here.

def home(request): 
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else: 
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration/password_change_don')
    else: 
        form = PasswordChangeForm(User)
    return render(request, 'registration/password_change_don.html', {
        'form': form
    })


def password_change_don(request):
    return render(request, 'registration/password_change_don.html')