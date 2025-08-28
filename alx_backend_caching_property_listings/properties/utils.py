from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Return all properties, cached in Redis for 1 hour.
    """
    properties = cache.get("all_properties")

    if not properties:
        # Fetch from DB if not cached
        properties = list(
            Property.objects.all().values(
                "id", "title", "description", "price", "location", "created_at"
            )
        )
        # Cache it for 1 hour (3600 seconds)
        cache.set("all_properties", properties, 3600)

    return properties
