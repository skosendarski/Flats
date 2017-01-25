from django.contrib import admin
from .models import City, Flat


# Register your models here.


def make_available(self, request, queryset):
    queryset.update(status='a', nickname=None, rented_from=None, rented_to=None)
    make_available.short_description = "Set as available"


def make_not_available(self, request, queryset):
    queryset.update(status='n')
    make_available.short_description = "Set as not available"


class FlatAdmin(admin.ModelAdmin):
    model = Flat
    list_display = ['id','city', 'street','number_of_building','number_of_flat','available_from','available_to',
                    'rented_from','rented_to','status','nickname']
    ordering = ['city', 'street','number_of_building','number_of_flat','available_from','available_to',
                'rented_from','rented_to','status','nickname']
    actions = [make_available, make_not_available]


admin.site.register(City)
admin.site.register(Flat,  FlatAdmin)