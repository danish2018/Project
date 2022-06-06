from django.shortcuts import render
from .models import Destination ,Contact
# Create your views here.


def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})

def contact(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Tell_us = request.POST['Tell_us']

        contact = Contact(Name = Name, Email = Email , Tell_us = Tell_us)
        contact.save()
    return render(request,'contact.html')
