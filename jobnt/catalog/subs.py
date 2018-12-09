from django.shortcuts import render
from .models import UserSubscription, Company, JobOffer
from django.http import HttpResponse

def index(request):
  args = {}

  if not request.user.is_authenticated:
    args['need_login'] = True
  else:
    # UserSubscription.
    subs = UserSubscription.objects.filter(user=request.user)
    offers = JobOffer.objects.all()
    
    subbed_companies = set()
    for sub in subs:
      subbed_companies.add(sub.company.id)

    args = {
        'need_login': False,
        'subs': subs,
        'no_subs': subs.count() == 0,
        'offers': offers,
        'subbed_companies': subbed_companies,
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

def favs(request):
  args = {}
  return render(request, 'catalog/favs.html', args)