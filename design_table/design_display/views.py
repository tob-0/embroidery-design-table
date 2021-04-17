from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CurrentImage

# Create your views here.

def index(request):
    current_image = CurrentImage.objects.all().first()
    template = loader.get_template('display/index.html')
    context = {
        'current_image': current_image,
    }
    return HttpResponse(template.render(context,request))

def change(request):
    current_url = CurrentImage.objects.all().first()
    context = {
        'current_url': current_url,
    }
    return HttpResponse(render(request,'display/change.html',context))


def post(request, ):
    if request.method == 'POST':
        new_url = request.POST['new_url']
        CurrentImage.objects.filter().update(url=new_url)
    return redirect('/design')