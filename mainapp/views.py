from turtle import pos
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import dataPost

# Create your views here.
@csrf_exempt
def getDataPostAll(request):
    dp = dataPost.objects.all()

    postContext = []

    for x in dp:
        pm = {'judul':x.judul, 'slug':x.slug, 'short_deks':x.short_deks, 'long_deks':x.long_deks, 'writer':x.writer, 'img':x.img_feature}
        postContext.append(pm)

    context = {
        'dataPost' : postContext
    }
    return JsonResponse(context, safe=False)

@csrf_exempt
def detailPost(request, slug):
    postDetail = dataPost.objects.filter(slug__contains=slug).first()
    context = {
        'isi' : postDetail.long_deks,
        'judul' : postDetail.judul,
        'img' : postDetail.img_feature,
        'writer' : postDetail.writer
    }
    return JsonResponse(context, safe=False)