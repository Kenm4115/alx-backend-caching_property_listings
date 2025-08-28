from .utils import get_redis_cache_metrics
from .utils import get_all_properties
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

# Cache for 15 minutes (60 * 15 seconds)


@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values(
        "id", "title", "description", "price", "location", "created_at"
    )
    return JsonResponse(list(properties), safe=False)


def property_list(request):
    properties = get_all_properties()
    return JsonResponse(properties, safe=False)


def cache_metrics(request):
    metrics = get_redis_cache_metrics()
    return JsonResponse(metrics)
