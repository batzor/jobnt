from django.shortcuts import render

def index(request):
  args = {'subs': ['aah', 'thats', 'hot', 'thats', 'hot']}
  return render(request, 'catalog/subs.html', args)

def favs(request):
  args = {}
  return render(request, 'catalog/favs.html', args)