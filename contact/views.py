from django.shortcuts import render
from contact.forms import ContactForm


# Create your views here.
def contact(request):
    if request.POST:
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()

        context = {'contactform': contact_form, 'message': True}

    else:
        contact_form = ContactForm()
        context = {'contactform': contact_form}

    return render(request, 'contact/contact.html', context)
