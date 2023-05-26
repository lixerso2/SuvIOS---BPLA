from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_auth_oidc.views import perform_login
from django.contrib import messages

User = get_user_model()

def home(request):
    return render(request, 'suvios/home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'suvios/signup.html')
    else:
        context = {}
        return render(request, 'suvios/signup.html', context=context)


def google_register(request):
    # Redirect the user to the Google authorization endpoint
    return redirect('https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20email%20profile')


def google_callback(request):
    # Verify the Google authorization code
    token = verify_token(request)
    if token:
        # Get the user's email and create a new user object in Django
        email = token.get('email')
        user, created = User.objects.get_or_create(username=email, email=email)
        # Log the user in using Django's authentication system
        login(request, user)
    # Redirect the user back to the homepage
    return redirect('/')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'suvios/index.html')
    else:
        context = {}
        return render(request, 'suvios/index.html', context=context)


