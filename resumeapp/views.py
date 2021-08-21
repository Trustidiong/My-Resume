from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method=="POST":
        contact=Contact()
        
        # TAKE NAMES OF THE FORM FIELDS
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        # sTORE THEM INTO THE CORRESPONDING FIELD IN THE MODEL
        contact.name=name
        contact.email=email
        contact.message=message
        
        contact.save()
        
        
        #return HttpResponse("<H3>Thanks for getting in touch</H3>")
    return render(request, 'index.html')