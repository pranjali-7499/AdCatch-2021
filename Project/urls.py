from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from Project import views

urlpatterns = [
    url(r'^upload$', views.TestUploadView.as_view()),
    url(r'^upload/success',
        TemplateView.as_view(template_name="all media.html"),
        name='upload_success'),
    url(r'^file/(?P<id>[0-9]+)$', views.file),
    path('',views.home,name='home'),
    path('my_projects',views.MyProject,name='my_projects'),
    path('resultmyproject',views.ResultMyProject,name='resultmyproject'),
    path('newproject',views.NewProject,name='newproject'),
    path('resultmyproject',views.ResultMyProject,name='resultmyproject'),
    path('all media',views.All_Media,name='all media'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)