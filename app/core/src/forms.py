from django import forms
from .pqrsf import pqrsf

#creamos las clases con los formularios pertinentes:

class ContactForm(forms.Form):
	#atributos del formulario de contacto
	tipomsj = forms.ChoiceField(label="Tipo de Petición", required=True, choices=pqrsf , widget=forms.Select(attrs={'class':'form-control'}))
	usuario = forms.CharField(label="Tu Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	correo = forms.EmailField(label="Correo Electronico", required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
	mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5'}))  
