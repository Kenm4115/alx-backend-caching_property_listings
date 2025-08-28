import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property

logger = logging.getLogger(__name__)

def get_all_properties():
    """
    Retrieve all properties from cache if available, otherwise fetch from DB and cache for 1 hour.
    """
    try:
        properties = cache.get("all_properties")
        if properties is None:
            properties = Property.objects.all()
            cache.set("all_properties", properties, 3600)
        return properties
    except Exception as e:
        logger.error(f"Error retrieving properties from cache: {e}")
        # fallback: return from DB without caching
        return Property.objects.all()


def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    """
    try:
        conn = get_redis_connection("default")
        info = conn.info("stats")

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total_requests = hits + misses

        hit_ratio = hits / total_requests if total_requests > 0 else 0

        metrics = {
            "hits": hits,
            "misses": misses,
            "hit_ratio": round(hit_ratio, 2),
        }

        logger.info(f"Redis Cache Metrics: {metrics}")
        return metrics
    except Exception as e:
        logger.error(f"Error retrieving Redis metrics: {e}")
        return {"hits": 0, "misses": 0, "hit_ratio": 0}
