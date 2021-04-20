from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.welcome),
    path("files",views.getFiles),
    path("upload",views.uploadFile),
    path("<int:param>",views.getFile),
    path("file/<int:param>",views.getAttachedFile),
    path("delete/<int:param>",views.deleteFile)
]