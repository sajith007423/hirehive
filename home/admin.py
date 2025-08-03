from django.contrib import admin
from . models import profile,courseOffer,jobOffer,interviewOffer
# Register your models here.
admin.site.register(profile)
admin.site.register(courseOffer)
admin.site.register(jobOffer)
admin.site.register(interviewOffer)
