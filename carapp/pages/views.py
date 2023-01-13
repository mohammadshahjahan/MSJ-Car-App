from django.shortcuts import render,redirect
from .models import *
from cars.models import Car
from django.contrib import messages

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    # search_fields = Car.objects.values('model','city','year','body_style')
    model_fields = Car.objects.values_list('model',flat=True).distinct()
    city_fields = Car.objects.values_list('city',flat=True).distinct()
    year_fields = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    data = {
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_fields':model_fields,
        'city_fields':city_fields,
        'year_fields':year_fields,
        'body_style_search':body_style_search,
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        entry = ContactForm(name=name,email=email,subject=subject,phone=phone,message=message)
        entry.save()
        messages.success(request,'Thank You for contacted us , we will reach you shortly! ')
        return redirect('contact')
        
    return render(request,'pages/contact.html')