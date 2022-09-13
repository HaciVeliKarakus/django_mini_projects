from django.shortcuts import render

from apps.cars.models import Driver, Car


def car_detail(request, pk):
    context = generate_context(pk)

    return render(request=request,
                  template_name='cars/car_details.html',
                  context=context)


def generate_context(pk=-1):
    if pk != -1:
        owner_obj = Driver.objects.get(pk=pk)
        car_objs = Car.objects.filter(owner_id=owner_obj.id)
    else:
        owner_obj = Driver.objects.all()
        car_objs = Car.objects.all()

    context = {
        'vehicles': car_objs,
        'drivers': owner_obj,
    }
    return context


def all_cars(request):
    context = generate_context()

    return render(request=request,
                  template_name='cars/car_details.html',
                  context=context)
