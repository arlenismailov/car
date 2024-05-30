from django.contrib import admin
from .models import *


admin.site.register(CarorSpareparts)
admin.site.register(Brand)
admin.site.register(Model)


class PhotoEventsInline(admin.TabularInline):
    model = PhotoEvents
    extra = 1


@admin.register(Product)
class EventsAdmin(admin.ModelAdmin):
    inlines = [PhotoEventsInline]