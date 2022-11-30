from  django.urls import path
from  django.contrib import admin
from .views import *
from django.urls import re_path as url
from django.urls import path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import  static
from django.conf import settings
from django.conf.urls.static import static
from homepage import views as uploader_views



urlpatterns=[
	path("",Home,name="home"),
	path("download1/",Download,name="download"),
	# path("sendFile/",SendFile,name="home"),


	url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
