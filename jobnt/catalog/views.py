from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import JobSearchForm
from .models import JobOffer

# Create your views here.
def index(request):
  form = JobSearchForm()
  offers = JobOffer.objects.all()
  args = {'form': form, 'offers': offers}
  return render(request, 'catalog/index.html', args)

def search(request):
  form = JobSearchForm(request.GET)
  if form.is_valid():
    return show_offers(form.cleaned_data)
  else:
    return HttpResponse('something is wrong')

def make_filters(data):
  name = data['name_field'] # str
  deadline = data['deadline_date_field'] # datetime.date
  location = data['location_field'] # str
  min_salary = data['salary_field'] # int
  duration = data['duration_field'] # int
  date_posted = data['date_posted_field'] # datetime.date
  filters = dict()
  if name:
    filters['name__icontains'] = name
  if deadline:
    filters['deadline__gte'] = deadline
  if location:
    filters['location__iexact'] = location
  if min_salary:
    filters['salary__gte'] = min_salary
  if duration: 
    filters['duration__gte'] = duration
  if date_posted:
    filters['date_posted__gte'] = date_posted
  return filters 

def show_offers(data):
  offers = JobOffer.objects.filter(**make_filters(data)).select_related()
  page = render_to_string('catalog/joboffers.html', {'offers': offers})
  return HttpResponse(page)