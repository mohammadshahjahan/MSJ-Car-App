from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .models import Car
# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_fields = Car.objects.values_list('model',flat=True).distinct()
    city_fields = Car.objects.values_list('city',flat=True).distinct()
    year_fields = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    data = {
        'cars':paged_cars,
        'model_fields':model_fields,
        'city_fields':city_fields,
        'year_fields':year_fields,
        'body_style_search':body_style_search,
    }
    return render(request,'cars/cars.html',data)

def car_detail(request,id):
    single_car = get_object_or_404(Car,pk=id)
    data = {
        'single_car':single_car,
    }
    return render(request,'cars/car_detail.html',data)

def search(request):
    cars = Car.objects.order_by('-created_date')
    model_fields = Car.objects.values_list('model',flat=True).distinct()
    city_fields = Car.objects.values_list('city',flat=True).distinct()
    year_fields = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(decription__icontains=keyword)

    if 'model' in request.GET:
        keyword = request.GET['model']
        if keyword:
            cars = cars.filter(model__iexact=keyword)
    
    if 'year' in request.GET:
        keyword = request.GET['year']
        if keyword:
            cars = cars.filter(year__iexact=keyword)
    
    if 'city' in request.GET:
        keyword = request.GET['city']
        if keyword:
            cars = cars.filter(city__iexact=keyword)
    
    if 'body_style' in request.GET:
        keyword = request.GET['body_style']
        if keyword:
            cars = cars.filter(body_style__iexact=keyword)

    if 'min_price' in request.GET:
        k = request.GET['min_price']
        j = request.GET['max_price']
        if k:
            cars = cars.filter(price__gte= k,price__lte =j)


    data = {
        'cars':cars,
        'model_fields':model_fields,
        'city_fields':city_fields,
        'year_fields':year_fields,
        'body_style_search':body_style_search,
    } 
    return render(request,'cars/search.html',data)