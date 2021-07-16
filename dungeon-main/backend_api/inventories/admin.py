from django.contrib import admin

from inventories.models import Item, Inventory


@admin.register(Item)
class ItemSettings(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
    )
    list_filter = (
        'name',
        'is_active',
    )


admin.site.register(Inventory)
