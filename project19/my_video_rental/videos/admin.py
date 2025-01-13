from django.contrib import admin
from . import models

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']

    search_fields = ['title']

    list_filter = ['release_year', 'length', 'title']

    list_display = ['title', 'release_year', 'length']

    list_editable = ['length']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name' + ' ' + 'last_name']

admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)