from django.urls import path
from . import views

urlpatterns = [
    path('', views.hod_home, name='hod_home'),
]