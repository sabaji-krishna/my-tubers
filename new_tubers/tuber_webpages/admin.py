from django.contrib import admin
from .models import Slider, Team, ContactInfo, Services
from django.utils.html import format_html


class ContactAdmin(admin.ModelAdmin):
    list_display = ('emial', 'phone')


class SliderAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="80" height="50" />'.format(object.photo.url))

    list_display = ('headline', 'button_text', 'myphoto')


class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'role')
    list_filter = ('role',)


admin.site.register(Services)
admin.site.register(ContactInfo, ContactAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
