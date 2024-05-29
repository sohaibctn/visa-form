from django.urls import path
from .import views


urlpatterns = [
    path('apply/', views.visa_appliaction, name='visa_application'),
    path('success/', views.success, name= 'success'),
]