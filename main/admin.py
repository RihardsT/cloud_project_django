from django.contrib import admin

# Register your models here.
from .models import Welcome

class WelcomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Welcome, WelcomeAdmin)