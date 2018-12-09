from django.urls import path
from . import views
from . import subs
from . import favs

urlpatterns = [
  path('', views.index, name='index'),
  path('search/', views.search, name='search'),
  path('subs/', subs.index, name='subs'),
  path('favs/', favs.index, name='favs'),
  path('add_sub/', subs.add_sub, name='add_sub'),
  path('rem_sub/', subs.rem_sub, name='rem_sub'),
  path('add_fav/', favs.add_fav, name='add_fav'),
  path('rem_fav/', favs.rem_fav, name='rem_fav'),
]
