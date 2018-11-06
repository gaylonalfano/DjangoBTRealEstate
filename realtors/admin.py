from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # Note the ","
    list_per_page = 25


# Don't forget to add/pass the new RealtorAdmin class:
admin.site.register(Realtor, RealtorAdmin)
