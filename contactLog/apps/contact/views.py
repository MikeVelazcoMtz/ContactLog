from django.shortcuts import render
from django.views.generic import FormView
from braces.views import LoginRequiredMixin

from .models import Contacts
from .forms import ContactForm


class ContactView(LoginRequiredMixin, FormView):
    template_name = 'pretty.html'
    form_class = ContactForm
    success_url = '/contact/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['items'] = Contacts.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        success = False
        if form.is_valid():
            form.save()
            success = True

        return render(request, self.template_name, {'form': form, 'success': success})

    def form_invalid(self, form_contact):
        return self.render(
            self.get_context_data(form_contact=form_contact,))

    def form_valid(self, form):
        return super(ContactView, self).form_valid(form)
