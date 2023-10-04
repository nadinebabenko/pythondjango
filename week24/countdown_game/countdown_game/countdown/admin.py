from django.contrib import admin
from .models import HighScore, Word

# Register your models here.
class WordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Word, WordAdmin)

class WordAdmin(admin.ModelAdmin):
    list_display = ('word_text', 'word_length')
