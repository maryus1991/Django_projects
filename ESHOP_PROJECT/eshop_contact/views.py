from django.shortcuts import render
from .forms import CreateContactForm
from .models import ContactUs
from eshop_settings.models import SiteSetting


def contact_us(request):
    sended = False
    contact_form = CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        fullname = contact_form.cleaned_data.get('fullname')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(fullname=fullname, email=email, subject=subject, text=text)
        sended = True

    contact_form = CreateContactForm()
    informations = SiteSetting.objects.first()
    context = {
        'contact_form': contact_form,
        'sended': sended,
        'informations': informations
    }
    return render(request, 'contact-us.html', context)
