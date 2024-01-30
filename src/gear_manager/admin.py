from django.contrib import admin

from . import models


class CustomUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.Category)
admin.site.register(models.GearListItem)
admin.site.register(models.GearList)
