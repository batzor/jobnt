from django import forms
from django.utils import timezone
from .models import JobOffer
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, MultiWidgetField

class JobSearchForm(forms.Form):
  # Be sure to check whether fields match respective ones located in models.py
  
  # Form fields
  name_field = forms.CharField(
    label=False,
    max_length=200,
    required=False)
  date_field = forms.DateField(
    label='Deadline',
    widget=forms.SelectDateWidget,
    required=False)
  location_field = forms.CharField(
    label='Location',
    max_length=200,
    required=False)

  # Setting the layout of the form 
  helper = FormHelper()
  helper.form_method = 'GET'
  helper.add_input(Submit('search', 'Search'))
  helper.layout = Layout(
    Field('name_field', placeholder='Enter keyword(s)'),
    MultiWidgetField(
      'date_field', 
      attrs=(
        {'style': 'width: 33%; display: inline-block;'})
    ),
    'location_field'
  )
    
