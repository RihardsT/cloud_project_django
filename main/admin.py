from django.contrib import admin

# Register your models here.
from .models import PageDescription

class PageDescriptionAdmin(admin.ModelAdmin):
    pass

admin.site.register(PageDescription, PageDescriptionAdmin)