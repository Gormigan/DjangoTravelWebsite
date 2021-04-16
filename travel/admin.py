from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from travel.models import Airport, Continent, Country, City, Hotel, Travel, Order


class ContinentAdmin(GroupAdmin):

    list_display = ('name',)
    search_fields = ("name",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class HotelAdmin(GroupAdmin):

    list_display = ('name',"standard","city")
    search_fields = ("name",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class TravelAdmin(GroupAdmin):

    list_display = ('name',"hotel","city_to","city_from","type")
    search_fields = ("name",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class OrderAdmin(GroupAdmin):

    list_display = ('travel',"first_name","email","price")
    search_fields = ("travel","first_name","email")
    ordering = ("travel",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Airport, ContinentAdmin)
admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, ContinentAdmin)
admin.site.register(City, ContinentAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Travel, TravelAdmin)
admin.site.register(Order, OrderAdmin)
# Register your models here.
