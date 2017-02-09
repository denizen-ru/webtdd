from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages, auth
from django.core.urlresolvers import reverse

from accounts.models import Token

SUCCESS_MESSAGE = "Check your email, we've sent you a link you can use to log in."


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token={uid}'.format(uid=str(token.uid))
    )
    message_body = 'Use this link to log in:\n\n{url}'.format(url=url)
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email]
    )
    messages.success(request, SUCCESS_MESSAGE)
    return redirect('/')


def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')
