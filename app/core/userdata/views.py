from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.urls import reverse



class NosotrosPageView(TemplateView):
    
    template_name = "nosotros.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{'tituloNo': '¿Quienes Somos?', 
                                                    'sebnomb': 'Sebastián Álvarez Pérez',
                                                    'desback':'Desarrollador Backend',
                                                    'sebcorreo':'alvarezperezsebastian2014@gmail.com',
                                                    'tomnomb':'Tomas Díaz Vásquez',
                                                    'desfront':'Desarrollador Frontend',
                                                    'tomcorreo':'samot0051@gmail.com',
                                                    'kevnomb':'Kevin Alexander Suaza Gómez',
                                                    'kevcorreo':'kealsugo@gmail.com'})
