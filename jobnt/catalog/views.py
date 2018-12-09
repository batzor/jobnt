from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import JobSearchForm, ProfileForm
from .models import JobOffer, UserSubscription, Favorite
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
    return show_offers(form.cleaned_data, request)
  else:
    return HttpResponse('something is wrong')

def make_filters(data):
  name = data['name_field'] # str
  deadline = data['deadline_date_field'] # datetime.date
  location = data['location_field'] # str
  min_salary = data['salary_field'] # int
  duration = data['duration_field'] # int
  date_posted = data['date_posted_field'] # datetime.date
  tag = data['tag_field'] # Tag object
  print(tag)
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
  if tag:
    filters['jobtag__tag'] = tag
  return filters 

def show_offers(request, data):
  offers = JobOffer.objects.filter(**make_filters(data)).select_related()
  
  subs = UserSubscription.objects.filter(user__exact=request.user)
  subbed_companies = set()
  for sub in subs:
    subbed_companies.add(sub.company.id)

  favs = Favorite.objects.filter(user=request.user)
  favved_offers = set()
  for fav in favs:
    favved_offers.add(fav.job.id)

  args = {
      'offers': offers,
      'favved_offers': favved_offers,
      'subbed_companies': subbed_companies,
      'user': request.user
    }
  page = render_to_string('catalog/joboffers.html', args)
  return HttpResponse(page)

def register(request):
  if request.method == 'POST':
    user_form = UserCreationForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.refresh_from_db()
      user.profile.status = profile_form.cleaned_data.get('status')
      user.profile.phone_number = profile_form.cleaned_data.get('phone_number')
      user.profile.occupation = profile_form.cleaned_data.get('occupation')
      user.save()
      username = user_form.cleaned_data['username']
      raw_password = user_form.cleaned_data['password1']
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('/catalog/')
  else:
    user_form = UserCreationForm()
    profile_form = ProfileForm()
  
  return render(request, 'catalog/register.html', {
      'form': user_form,
      'pro_form': profile_form
    })
