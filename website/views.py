from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.http import BadHeaderError, HttpResponse
from .forms import *
from django.conf import settings
from django.db.models import Q


def homepage(request):
    bike=Specfication.objects.all()[6:]
    context={
        'bikes':bike
    }
    return render(request,'home.html',context)

def booking(request):
    query = request.GET.get('q')
  
    
    if query:
        bike = Specfication.objects.filter(
            Q(bike__name__icontains=query) |
            Q(bike__company__icontains=query) |
            Q(bike__model__icontains=query)
        )
        print(bike)
    else:
        bike=Specfication.objects.all()
    context={
        
        'bikes':bike
    }
    return render(request,'booking.html',context)



def bike_detail(request, bike_id):
    specification = get_object_or_404(Specfication, pk=bike_id)
    if request.method == 'POST':
        print("Post form")
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'name': form.cleaned_data['name'],
            'ph': form.cleaned_data['ph'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message'],
            }
            
            email_header = "A new client is trying to contact you:"
            # message = "\n".join([email_header] + [f"{key}: {value}" for key, value in body.items()])
            # response = "Your message has been sent. Thank you!"

            #Email to User
            bike=specification.bike.name
            subject = "Received Inquiry"
            message = f"Hi {body.get('name')}, we have received your email regarding the bike {bike}"
            email = body.get('email')

            #Email to Comapny
            subject_company = f"(Website Inquiry) "+bike
            message_company = "\n".join([email_header] + [f"Name:\n{body.get('name')} \n\nMessage: \n{body.get('message')}"])
            

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER,[email])

                #Email to Company
                send_mail(subject_company, message_company, email,[settings.EMAIL_HOST_USER])
                messages.success(request, "Message sent!")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return redirect('contact')
        else:
            print(form.errors)
    
    
    
    form = ContactForm()
    
    context = {
           'form':form,
        'specification': specification
    }
    return render(request, 'detail.html', context)

