from django.urls import path
from . import views
from . import subs

urlpatterns = [
  path('', views.index, name='index'),
  path('search/', views.search, name='search'),
  path('subs/', subs.index, name='subs'),
]
