from django.contrib import admin

from .models import Car, Shop, Manufacturer, Repair

# Register your models here.

class RepairAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RepairAdmin, self).save_model(request, obj, form, change)


class ShopAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('information', )

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

class CarAdmin(admin.ModelAdmin):
    list_display = ('type', 'max_speed',)


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Repair, RepairAdmin)
admin.site.register(Shop, ShopAdmin)