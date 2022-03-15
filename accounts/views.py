from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect




def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')
        
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('core:home')
    else:
        form = AuthenticationForm()
        
    context = {
        'title': "Zaloguj się",
        'form': form
    }
    return render(request, "accounts/login.html", context)


def register_view(request):
    if request.user.is_authenticated: 
        return redirect('core:home')
        
    print(request.user.is_authenticated)
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:home')
    else:
        form = UserCreationForm()
        
    context = {
        'title': "Zarejestruj się",
        'form': form
    }
    return render(request, "accounts/register.html", context)


@login_required
def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('core:home')
