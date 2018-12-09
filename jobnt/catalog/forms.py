from django import forms
from django.utils import timezone
from .models import JobOffer
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions, Accordion, AccordionGroup
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, MultiWidgetField

class JobSearchForm(forms.Form):
  # Be sure to check whether fields match respective ones located in models.py
  
  # Form fields
  name_field = forms.CharField(
    label=False,
    required=False,
    max_length=200)
  deadline_date_field = forms.DateField(
    label=False,
    required=False,
    widget=forms.SelectDateWidget)
  location_field = forms.CharField(
    label=False,
    required=False,
    max_length=200)
  salary_field = forms.IntegerField(
    label=False,
    required=False)
  duration_field = forms.IntegerField(
    label=False,
    required=False)
  date_posted_field = forms.DateField(
    label=False,
    required=False,
    widget=forms.SelectDateWidget)
  # Setting the layout of the form 
  helper = FormHelper()
  helper.form_method = 'GET'
  helper.form_id = 'search-form'
  helper.form_action = 'search/'
  helper.add_input(Submit('search', 'Search'))
  helper.layout = Layout(
    Field('name_field', placeholder='What do you want to do?'),
    Accordion(
      AccordionGroup('Deadline',
        MultiWidgetField(
          'deadline_date_field', 
          attrs=(
            {'style': 'width: 33%; display: inline-block;'})
        )
      ),
      AccordionGroup('Location',
        Field('location_field', placeholder='Type in location where you would like to work')
      ),
      AccordionGroup('Salary',
        Field('salary_field', placeholder='Type in minimal salary')
      ),
      AccordionGroup('Duration',
        Field('duration_field', placeholder='Type in minimal duration of the job (in weeks)')
      ),
      AccordionGroup('Date posted', 
        MultiWidgetField(
          'date_posted_field', 
          attrs=(
            {'style': 'width: 33%; display: inline-block;'})
        )
      )
    )
  )
