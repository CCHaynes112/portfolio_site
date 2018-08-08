from django.shortcuts import render
from django.http import *
from django.core.mail import send_mail

from .forms import EmailForm


def index(request):
    form = EmailForm
    return render(request, 'portfolio/home.html', {'form': form})


def send_mail_func(request):

    form = EmailForm(data=request.POST)
    if form.is_valid():
        # Send email:
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        body = form.cleaned_data['body']

        body = "From: " + email + "\n\n" + body

        recipient = ['CCHaynes1122@gmail.com']

        send_mail(
            'Website Mail: From: ' + name,
            body,
            email,
            recipient,
        )
        return HttpResponse("pass")
    return HttpResponse("fail")
