from django.contrib import admin
from . models import TuberContact


class Ctuber(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')

admin.site.register(TuberContact, Ctuber)

