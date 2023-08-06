from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """ Display view for the contact form """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            email_address = contact_form.cleaned_data['email_address']
            message = contact_form.cleaned_data['message']
            contact_form.save()

            try:
                send_mail(
                    f'Message from {email_address}',
                    message,
                    email_address,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,  # Raise an SMTPException if it fails
                )
                messages.success(
                    request,
                    'Thank you for contacting us!')
                return HttpResponseRedirect('/contact/')

            except BadHeaderError:
                return HttpResponse('Invalid header found')

        else:
            messages.error(request, 'Failed to send your message.\
                    Please check if the form is valid')
            return redirect(reverse, 'contact')

    else:
        if request.user.is_authenticated:
            contact_form = ContactForm(
                initial={'email_address': request.user.email}
            )
        else:
            contact_form = ContactForm()
    context = {
            'contact_form': contact_form,
            }
    return render(request, 'contact/contact.html', context)
