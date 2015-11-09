from django.http import HttpResponse
from django.shortcuts import render

from .models import Treasure


def index(request):
    treasures = Treasure.objects.order_by('-pub_date')[:20]
    context = {'treasures': treasures}
    return render(request, 'scooper/index.html', context)
