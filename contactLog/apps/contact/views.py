from django.shortcuts import render
from django.views.generic import FormView
from braces.views import LoginRequiredMixin

from .models import Contacts
from .forms import ContactForm


class ContactView(LoginRequiredMixin, FormView):
    template_name = 'pretty.html'
    form_class = ContactForm
    success_url = 'contact/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['items'] = Contacts.objects.all()
        return context
