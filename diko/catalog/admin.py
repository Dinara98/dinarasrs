from django.contrib import admin

# Register your models here.
from .models import Guest, Eating, Menu

#admin.site.register(Menu)
#admin.site.register(Guest)
admin.site.register(Eating)

# Define the admin class
class GuestAdmin(admin.ModelAdmin):
 list_display = ('last_name', 'first_name', 'time_of_order')
# Register the admin class with the associated model
admin.site.register(Guest, GuestAdmin)

# Register the Admin classes for Menu using the decorator

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
     list_display = ('name', 'guest')
