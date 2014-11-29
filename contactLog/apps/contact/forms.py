# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from .models import Contacts
from apps.locations.models import Ciudad, Sucursal


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '1'}), required=True)
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '2'}), required=False)
    num_ext = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '3'}), required=False)
    colonia = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '4'}), required=False)
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'tabindex': '5'}), required=False)
    ciudad = forms.ModelChoiceField(required=True, queryset=Ciudad.objects.all(), empty_label=u'Seleccione',
                                    widget=forms.Select(attrs={'class': 'w100', 'tabindex': '6', }))
    sucursal = forms.ModelChoiceField(required=True, queryset=Sucursal.objects.all(), empty_label=u'Seleccione',
                                    widget=forms.Select(attrs={'class': 'w100', 'tabindex': '6', }))

    class Meta:
        model = Contacts
        exclude = {'sucursales', }
