from django import forms
from .models import JobOffer
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, MultiWidgetField

class JobSearchForm(forms.Form):
  #Be sure to check whether fields match respective ones located in models.py
  name_field = forms.CharField(max_length = 200)
  date_field = forms.DateField(widget=forms.SelectDateWidget)
  location_field = forms.CharField(max_length = 200)
  helper = FormHelper()
  helper.layout = Layout(
    'name_field',
    MultiWidgetField('date_field', attrs=({'style': 'width: 33%; display: inline-block;'})),
    'location_field',
    FormActions(
      Submit('search', 'Search', css_class='btn-primary')
    )
  )
    
