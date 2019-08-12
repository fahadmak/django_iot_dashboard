from django.contrib.auth.decorators import login_required
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from iot_dashboard import settings
from iot_dashboard.apps.dashboard.services import get_channel

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@login_required
@cache_page(CACHE_TTL)
def dashboard(request):
    return render(request, 'dashboard/index.html', {'feeds': get_channel()})
