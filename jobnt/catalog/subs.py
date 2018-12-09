from django.shortcuts import render
from .models import UserSubscription

def index(request):
  args = {}

  if not request.user.is_authenticated:
    args['need_login'] = True
  else:
    # UserSubscription.
    my_subs = UserSubscription.objects.filter(user__exact=request.user.id)
    args = {'my_subs': my_subs}

  return render(request, 'catalog/subs.html', args)

def add_sub(request):
  user_id = request.user.id
  company_id = request.GET['company_id']
  return company_id

  # exists = UserSubscription.filter(user__exact=my_id, company__exact=company_id).count() > 0
  #
  # if exists:
  #   return "already subscribed"
  # else:
  #   sub = UserSubscription.create(user=my_id, company=company_id)
  #   sub.save()
  #   return "success"

def favs(request):
  args = {}
  return render(request, 'catalog/favs.html', args)