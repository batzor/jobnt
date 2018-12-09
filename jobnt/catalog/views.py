from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import JobSearchForm
from .models import JobOffer, UserSubscription
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
  form = JobSearchForm()
  offers = JobOffer.objects.all()
  args = {'form': form, 'offers': offers}
  return render(request, 'catalog/index.html', args)

def search(request):
  form = JobSearchForm(request.GET)
  if form.is_valid():
    return show_offers(request, form.cleaned_data)
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

def show_offers(request, data):
  offers = JobOffer.objects.filter(**make_filters(data)).select_related()
  
  subs = UserSubscription.objects.filter(user__exact=request.user)
  subbed_companies = set()
  for sub in subs:
    subbed_companies.add(sub.company.id)

  page = render_to_string('catalog/joboffers.html', {'offers': offers, 'subbed_companies': subbed_companies})
  return HttpResponse(page)

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      raw_password = form.cleaned_data['password1']
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('/catalog/')
  else:
    form = UserCreationForm()
  return render(request, 'catalog/register.html', {'form': form})
