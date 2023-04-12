from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def cursoFormulario(request):
    
    
     return render(request, "cursoFormulario.html")


def Contact(request):
    contact_form = ContactForm()
    return render(request, 'contact/contact.html', {'form': contact_form})
