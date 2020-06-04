from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('contactenos/',views.contacto, name ='contactenos'),
]