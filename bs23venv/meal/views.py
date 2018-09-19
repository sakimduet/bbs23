
from django.shortcuts import render


from .models import Registrationf


# Create your views here.
def index (request):
    return render(request,"index.html")
def menu (request):
    return render(request,"menu.html")
def Registration(request):
    if request.method == 'POST':
        if request.POST.get('firstName') and request.POST.get('lastName')and request.POST.get('email') and request.POST.get('phnNum')and request.POST.get('password'):
           reg=Registrationf()
           reg.firstName=request.POST.get('firstName')
           reg.lastName = request.POST.get('lastName')
           reg.email= request.POST.get('email')
           reg.phnNum = request.POST.get('phnNum')
           reg.password=request.POST.get('password')
           reg.save()
           return render(request, "Registration.html")
    else:

        return render(request,"Registration.html")
