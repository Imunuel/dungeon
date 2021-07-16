def create_user_inventory(sender, instance, created, **kwargs):
    if created:
        from .models import Inventory
        Inventory.objects.create(user=instance)
