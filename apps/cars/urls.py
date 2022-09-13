from django.urls import path

from apps.cars import views

urlpatterns = [
    path('', views.all_cars, name='all_cars'),
    path('<int:pk>', views.car_detail, name='car_detail'),
]
