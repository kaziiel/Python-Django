from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request,*args, **kwargs):
        return render(request, self.template_name,{'eslogan':'Tu mejor opción.',
                                                    'primerPa':'Digital market es un plataforma de ventas para un supermercado acogiendo un diseño acogedor y fácil de usar para el usuario, la plataforma contará con diversas opciones tanto para el usuario y administrador.'})
                                                        

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



def contacto(request):
    formContact = ContactForm()
    
    
    #Validar que el formulario tenga una peticion post:
    if request.method == "POST":
        #Reconfiguramos formContact con los datos que hemos enviado, es decir rellenamos la plantilla con el formulario
        formContact = ContactForm(data=request.POST)
        if formContact.is_valid():
            tipomsj = request.POST.get('tipomsj', '')
            usuario = request.POST.get('usuario', '')
            correo = request.POST.get('correo', '')
            mensaje = request.POST.get('mensaje', '')
            
            #Creamos el objeto con las variables del formulario
            email = EmailMessage(
                "RepoDevelopers: tienes un nuevo mensaje de contacto",
                "De: {} <{}>\n\nEscribio:\n\nTipo de Mensaje:{}\n{}".format(usuario,correo, tipomsj ,mensaje),
                "no-contestar@inbox.mailtrap.io",
                ["samot0051@gmail.com"],
                reply_to=[correo]
            )
            #Enviamos el correo:
            try:
                email.send()
                return redirect(reverse('contactenos')+"?ok")
            except:
                #No se ha enviado el correo
                return redirect(reverse('contactenos')+"?fail")
            
    return render(request,'contactenos.html',{'formulario':formContact})



		
