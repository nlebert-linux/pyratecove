from django.shortcuts import render
from contact.forms import ContactForm


# Create your views here.
def contact(request):
    if request.POST:
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()

        else:
            context = {'contactform': contact_form, 'errors': contact_form.errors}
            return render(request, 'contact/contact.html', context)

        context = {'contactform': contact_form, 'message': True}

    else:
        contact_form = ContactForm()
        context = {'contactform': contact_form}

    return render(request, 'contact/contact.html', context)


def resume(request):
    return render(request, 'contact/resume.html')
