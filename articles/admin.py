from django.contrib import admin
from .models import Articles,Tag

# Register your models here.

admin.site.register(Articles)
admin.site.register(Tag)