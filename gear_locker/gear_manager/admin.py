from django.contrib import admin

from . import models


admin.site.register(models.Category)
admin.site.register(models.GearListItem)
admin.site.register(models.GearList)
