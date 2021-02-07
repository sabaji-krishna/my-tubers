from django.contrib import admin
from . models import Hiretuber


class Htuber(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'tuber_name')


admin.site.register(Hiretuber, Htuber)

