from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from proyecto_django.forms import ContactForm

# def cursoFormulario(request):
    
    
#      return render(request, "cursoFormulario.html")


def Contact(request):
    contact_form = ContactForm()
    return render(request, 'contact/contact.html', {'form': contact_form})

