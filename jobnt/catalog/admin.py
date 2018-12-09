from django.contrib import admin
from catalog import models

admin.site.register(models.Profile)
admin.site.register(models.UserSubscription)
admin.site.register(models.Company)
admin.site.register(models.JobOffer)
admin.site.register(models.Favorite)
admin.site.register(models.Tag)
admin.site.register(models.JobTag)
