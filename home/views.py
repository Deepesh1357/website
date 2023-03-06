from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Services
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request): 
    if request.method == "POST":  
        desc = request.POST.get('desc')
        services = Services(desc=desc,date = datetime.today())
        services.save()
        messages.success(request, 'Your query has been sent, our team will reach you soon!')
    return render(request, 'services.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Thanks for your review.')
    return render(request, 'contact.html')
 