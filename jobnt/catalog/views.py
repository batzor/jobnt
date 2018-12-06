from django.shortcuts import render
from .forms import JobSearchForm
from .models import JobOffer

# Create your views here.
def index(request):
  form = JobSearchForm(request.GET)
  if form.is_valid():
    name = form.cleaned_data['name_field']
    deadline = form.cleaned_data['date_field']
    location = form.cleaned_data['location_field']
    offers = JobOffer.objects.all() 
    if name:
      pass
    if deadline:
      pass
    if location:
      pass
    args = {'form': form, 'offers': offers}
    return render(request, 'catalog/index.html', args)
  return render(request, 'catalog/index.html', {'form': form})
