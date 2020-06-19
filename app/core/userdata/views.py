from django.shortcuts import render
from django.views.generic.list import ListView 
from .models import DatosUser
from django.utils import timezone





class NosotrosListView(ListView):
    template_name = "nosotros.html"
    model = DatosUser
    paginate_by = 100 #if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
