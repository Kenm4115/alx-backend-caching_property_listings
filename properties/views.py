from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
from .utils import get_all_properties, get_redis_cache_metrics

@cache_page(60 * 15)  # Cache response for 15 minutes
def property_list(request):
    properties = get_all_properties()
    data = list(properties.values())  # Convert queryset to list of dicts
    return JsonResponse({"data": data}, safe=False)


def cache_metrics(request):
    metrics = get_redis_cache_metrics()
    return JsonResponse({"data": metrics}, safe=False)
