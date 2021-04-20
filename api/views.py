from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from os import scandir, path
import json

from .models import File
# Create your views here.

def welcome(request):
    return JsonResponse("Hello World!",safe=False)

@require_http_methods(['POST'])
def uploadFile(request):
    response= ""
    if request.FILES.getlist('file'):
        for element in request.FILES.getlist('file'):
            print(request.FILES.getlist('file'))
            name = element.name
            extension = element.name.split(".")[-1]
            capacity = element.size
            fs = FileSystemStorage()
            filename = fs.save(name,element)
            uploaded_file_url = fs.url(filename)
            receivedfile = File.objects.create(name=name,extension=extension,capacity=capacity,url=uploaded_file_url)
            receivedfile.save()
            response = "Successful Upload"
    else:
        response = "0 Files "
    return(JsonResponse(response,safe=False))

def deleteFile(request,param):
    fileToDelete = File.objects.get(id=param)
    fs = FileSystemStorage()
    fs.delete(fs.location +"/" + fileToDelete.name)
    fileToDelete.delete()
    return(JsonResponse('Deleted Complete',safe=False))

@require_http_methods(['GET'])
def getAttachedFile(request,param):
    file = File.objects.get(id=param)
    fs = FileSystemStorage()
    response = FileResponse(fs.open(fs.location+'/'+file.name,'rb'),content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename ={file.name}'
    return(response)

@require_http_methods(['GET'])
def getFiles(request):
    files = File.objects.all()
    data = list(files.values("id","name","extension","capacity","url"))
    return JsonResponse(data,safe=False)


@require_http_methods(['GET'])
def getFile(request,param):
    data = File.objects.filter(id=param)
    return JsonResponse(list(data.values("id","name","capacity","extension","url")),safe=False)