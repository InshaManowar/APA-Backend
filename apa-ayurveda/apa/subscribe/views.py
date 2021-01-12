from django.shortcuts import render
#from apa.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

# Create your views here.
#The EMAIL_HOST_USER and send_mail() method.



def subscribe (request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)  #checking if the data is get or post with the form object sub
        subject = 'Welcome to APA' 
        message = "Hope you are enjoying your journey"
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, 'isterecruitements2020@gmail.com', [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})

