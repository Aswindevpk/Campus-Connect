from django.contrib import admin
from .models import  Explore,Carousel,Bloodreq,News,Program,BloodDonation,Fests

# Register your models here.

admin.site.register(Bloodreq)
admin.site.register(Explore)
admin.site.register(News)
admin.site.register(Carousel)
admin.site.register(Program)
admin.site.register(Fests)
admin.site.register(BloodDonation)
