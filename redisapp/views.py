from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from .models import *
# Create your views here.
def home(request):
    payload=[]
    db=None

    if cache.get('fruits'):
        payload=cache.get('fruits')
        db="cache"
    else:
        objs=Fruits.objects.all()
        print("obh",objs)
        for obj in objs:
            payload.append(obj.fruits_name)
        db="sqlite"
        cache.set('fruits',payload, timeout=20)
    return JsonResponse({'status': 200,'db':db,'data':payload})