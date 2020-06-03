from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('', views.NosotrosPageView.as_view(), name='nosotros'),
    path('contactenos/',views.contacto, name ='contactenos'),
]