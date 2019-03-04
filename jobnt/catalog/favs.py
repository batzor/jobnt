from django.shortcuts import render
from .models import UserSubscription, Company, JobOffer, Favorite
from django.http import HttpResponse

def index(request):
  args = {}

  if not request.user.is_authenticated:
    args['need_login'] = True
  else:
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
        'favs': favs,
        'no_favs': favs.count() == 0,
        'favved_offers': favved_offers,
        'subbed_companies': subbed_companies,
      }

  return render(request, 'catalog/favs.html', args)

def add_fav(request):
  offer_id = request.GET['offer_id']
  user = request.user
  try:
    offer = JobOffer.objects.get(id=offer_id)
  except:
    return HttpResponse("Error: offer doesnt exist")
  
  exists = Favorite.objects.filter(user=user, job=offer).count() > 0
  
  if exists:
    return HttpResponse("OK: favorited (already)")
  else:
    fav = Favorite.objects.create(user=user, job=offer)
    fav.save()
    return HttpResponse("OK: favorited")

def rem_fav(request):
  offer_id = request.GET['offer_id']
  user = request.user
  try:
    offer = JobOffer.objects.get(id=offer_id)
  except:
    return HttpResponse("Error: offer doesnt exist")
  
  exists = Favorite.objects.filter(user=user, job=offer).count() > 0
  
  if exists:
    Favorite.objects.filter(user=user, job=offer).delete()
    return HttpResponse("OK: unfavorited")
  else:
    return HttpResponse("OK: not favorited")

def show_favs(request):
  if request.user.is_authenticated:
      user_favs = Favorite.objects.filter(user=request.user)
      offers = []
      for fav in user_favs:
          offers.append(fav.job)
      return render(request, 'catalog/favs.html', {'offers': offers})
  else:
      return render(request, 'accounts/login.html')
