from django.urls import path
from . import views
from . import subs

urlpatterns = [
  path('', views.index, name='index'),
  path('search/', views.search, name='search'),
  path('subs/', subs.index, name='subs'),
  path('favs/', subs.favs, name='favs'),
  path('add_sub/', subs.add_sub, name='add_sub'),
  path('rem_sub/', subs.rem_sub, name='rem_sub'),
]
