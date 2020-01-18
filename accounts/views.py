from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import auth, messages
from accounts.models import Token
import sys

def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
            reverse('login') + '?token=' + str(token.uid)
            )
    message_body = f'Please use this link to log in:\n\n{url}'
    send_mail('Your login link for Superlists',
            message_body,
            'noreply@superlists',
            [email]
        )
    messages.success(
            request,
            "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')

def login(request):
    print('login called',file=sys.stderr)
    print(f'token is {request.GET.get("token")}',file=sys.stderr)
    user = auth.authenticate(uid=request.GET.get('token'))
    if user is not None:
        print('login success',file=sys.stderr)
        auth.login(request, user)
    else:
        print('login failed',file=sys.stderr)
    return redirect('/')
