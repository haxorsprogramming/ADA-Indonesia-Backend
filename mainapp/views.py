from turtle import pos
from django.shortcuts import render
from django.http import JsonResponse

from .models import dataPost

# Create your views here.
def getDataPostAll(request):
    dp = dataPost.objects.all()

    postContext = []

    for x in dp:
        pm = {'judul':x.judul, 'slug':x.slug, 'short_deks':x.short_deks, 'long_deks':x.long_deks, 'writer':x.writer}
        postContext.append(pm)

    context = {
        'dataPost' : postContext
    }
    return JsonResponse(context, safe=False)