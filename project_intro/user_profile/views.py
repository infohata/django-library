from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if not (username and email and password1):
            messages.error(request, _('Incomplete form, all fields are required.'))
        elif password1 != password2:
            messages.error(request, _('Passwords do not match.'))
        elif User.objects.filter(username=username).exists():
            messages.error(request, _('Username already taken.'))
        elif User.objects.filter(email=email).exists():
            messages.error(request, _('User with this email already exists.'))
        else:
            user = User(username=username, email=email)
            user.set_password(password1)
            user.save()
            messages.success(request, _('User registration successful, you can login now.'))
            return redirect(reverse_lazy('login'))
    return render(request, 'user_profile/register.html')

@login_required
def profile(request):
    return render(request, 'user_profile/profile.html')
