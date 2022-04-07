from django.shortcuts import render, redirect
from email import message
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            message.success(request, f'Account created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {
        "form": form,
    })