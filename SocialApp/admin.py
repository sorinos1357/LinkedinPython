from django.contrib import admin
from SocialApp import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.CompanyProfile)
admin.site.register(models.Message)
admin.site.register(models.Notification)
admin.site.register(models.Post)
admin.site.register(models.Comment)
