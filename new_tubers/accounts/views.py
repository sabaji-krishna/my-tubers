from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from hiretubers.models import Hiretuber
from tuber_webpages.models import ContactInfo


def login(request):
    contact_info = ContactInfo.objects.all()
    data = {
        'contact_info': contact_info
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.warning(request, 'You are LoggedIn')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'accounts/login.html', data)


def register(request):
    contact_info = ContactInfo.objects.all()
    data = {
        'contact_info': contact_info
    }
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already Exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email already Exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
                                                    email=email, password=password)
                    user.save()
                    messages.success(request, 'Account Created Successfully')
                    return redirect('login')
        else:
            messages.warning(request, 'Password did not Match')
            return redirect('register')
    return render(request, 'accounts/register.html', data)


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    userid = request.user.id
    hiretuber = Hiretuber.objects.filter(id=userid)
    contact_info = ContactInfo.objects.all()
    data = {
        'hiretuber': hiretuber,
        'contact_info': contact_info
    }
    return render(request, 'accounts/dashboard.html', data)

