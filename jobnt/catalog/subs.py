from django.shortcuts import render
from .models import UserSubscription, Company, JobOffer, Favorite
from django.http import HttpResponse

def index(request):
  args = {}

  if not request.user.is_authenticated:
    args['need_login'] = True
  else:
    offers = JobOffer.objects.all()
    
    subs = UserSubscription.objects.filter(user=request.user)
    subbed_companies = set()
    for sub in subs:
      subbed_companies.add(sub.company.id)

    favs = Favorite.objects.filter(user=request.user)
    favved_offers = set()
    for fav in favs:
      favved_offers.add(fav.job.id)

    args = {
        'need_login': False,
        'subs': subs,
        'no_subs': subs.count() == 0,
        'offers': offers,
        'subbed_companies': subbed_companies,
        'favved_offers': favved_offers,
      }

  return render(request, 'catalog/subs.html', args)

def add_sub(request):
  company_id = request.GET['company_id']
  user = request.user
  try:
    company = Company.objects.get(id=company_id)
  except:
    return HttpResponse("Error: company doesnt exist")
  
  exists = UserSubscription.objects.filter(user__exact=user, company__exact=company).count() > 0
  
  if exists:
    return HttpResponse("OK: subscribed (already)")
  else:
    sub = UserSubscription.objects.create(user=user, company=company)
    sub.save()
    return HttpResponse("OK: subscribed")

def rem_sub(request):
  company_id = request.GET['company_id']
  user = request.user
  try:
    company = Company.objects.get(id=company_id)
  except:
    return HttpResponse("Error: company doesnt exist")
  
  exists = UserSubscription.objects.filter(user__exact=user, company__exact=company).count() > 0
  
  if exists:
    UserSubscription.objects.filter(user__exact=user, company__exact=company).delete()
    return HttpResponse("OK: unsubscribed")
  else:
    return HttpResponse("OK: not subscribed")