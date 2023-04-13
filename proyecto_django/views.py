from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def cursoFormulario(request):
    
    
      return render(request, "cursoFormulario.html")


# def Contact(request):
#     contact_form = ContactForm()
#     return render(request, 'contact/contact.html', {'form': contact_form})




from contact.models import Contact as ContactModel

def my_view(request):
    my_contacts = ContactModel.objects.all()
    # Resto del código



from .forms import ContactForm
# from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact_type = form.cleaned_data['contact_type']
            subscription = form.cleaned_data['subscription']
            
            # Create and save Contact object
            contact = Contact(
                name=name,
                email=email,
                message=message,
                contact_type=contact_type,
                subscription=subscription
            )
            contact.save()
            
            return redirect('contact')  # Redirect to the contact page
            
    else:
        form = ContactForm()
        
    return render(request, 'contact/contact.html', {'form': form})