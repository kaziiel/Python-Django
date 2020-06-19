from django.urls import path
from . import views
from .views import NosotrosListView


urlpatterns = [
    path('nosotros/', NosotrosListView.as_view(), name ='nosotros'),
]