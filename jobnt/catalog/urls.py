from django.urls import path
from . import views
from . import subs
from . import favs

urlpatterns = [
  path('', views.index, name='index'),
  path('search/', views.search, name='search'),
  path('subs/', subs.index, name='subs'),
  path('favs/', views.show_favs, name='favs'),
]
