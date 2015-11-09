from django.contrib import admin

from .models import Treasure, TreasureStatus


class TreasureAdmin(admin.ModelAdmin):
    fields = ['status', 'headline', 'content']


admin.site.register(TreasureStatus)
admin.site.register(Treasure, TreasureAdmin)
