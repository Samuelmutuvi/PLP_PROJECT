from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('capture/material/submit/', views.submit_materials, name='submit_materials'),
    path('capture/employee/submit/', views.submit_employees, name='submit_employees'),
]
