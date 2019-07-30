from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from iot_dashboard.apps.dashboard.services import get_channel


@login_required
def dashboard(request):
    channel = get_channel()
    return render(request, 'dashboard/index.html', {'feeds': channel['feeds']})

