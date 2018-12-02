from django.contrib import admin
from catalog.models import Company, JobOffer, Favorite, Tag

admin.site.register(Company)
admin.site.register(JobOffer)
admin.site.register(Favorite)
admin.site.register(Tag)
