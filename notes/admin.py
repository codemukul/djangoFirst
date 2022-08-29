from django.contrib import admin
from . import models

# Register your models here.
class Notesadmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Notes , Notesadmin)