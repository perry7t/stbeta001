from django.contrib import admin
from .models import Status, Site, SiteAddress, Shift, Shiftuser, Function, Customer

admin.site.register(Status)
admin.site.register(Site)
admin.site.register(SiteAddress)
admin.site.register(Shiftuser)
admin.site.register(Customer)


class ShiftAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'start_time', 'end_time', 'shift_title', 'site', 'user', 'status']


admin.site.register(Shift, ShiftAdmin)


class FunctionAdmin(admin.ModelAdmin):
    list_display = ['function_name', 'function_short']


admin.site.register(Function, FunctionAdmin)