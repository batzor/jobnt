from django.shortcuts import render
from .forms import JobSearchForm
from .models import JobOffer

# Create your views here.
def index(request):
  form = JobSearchForm()
  offers = JobOffer.objects.all()
  args = {'form': form, 'offers': offers}
  return render(request, 'catalog/index.html', args)