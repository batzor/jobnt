from django.shortcuts import render
from .forms import JobSearchForm

# Create your views here.
def index(request):
  form = JobSearchForm(request.GET)
  if form.is_valid():
    name = form.cleaned_data['name']
    #DEBUG
    #print(name)

  return render(request, 'catalog/index.html', {'form': form})
