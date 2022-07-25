from django.contrib import admin

from . import models

# Register your models here.
class WordListAdmin(admin.ModelAdmin):
    list_display = ['pk', 'gender', 'word']
    #allow us to update info inside the panel
    list_editable = [ 'gender', 'word']

admin.site.register(models.WordList, WordListAdmin)