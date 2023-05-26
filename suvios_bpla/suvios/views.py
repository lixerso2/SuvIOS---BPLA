
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_auth_oidc.views import perform_login
from django.contrib.auth import get_user_model

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
            return HttpResponseRedirect(reverse('secret_page'))
        else:
            return render(request, 'suvios/signup.html', {'error_message': 'Passwords do not match'})
    else:
        context = {}
        return render(request, 'suvios/signup.html', context=context)


User = get_user_model()

def google_register(request):
    # Redirect the user to the Google authorization endpoint
    return perform_login(request, authorization_endpoint=OIDC_OP_AUTHORIZATION_ENDPOINT, scopes=['openid', 'email', 'profile'])

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