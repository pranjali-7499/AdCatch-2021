from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from .models import Upload_File

from Project.forms import TestUploadForm
from Project.models import Upload_File

import django
from django.urls import reverse_lazy


class TestUploadView(FormView):
    template_name = 'uploadfile.html'
    form_class = TestUploadForm
    success_url = reverse_lazy('upload_success')
    
    def Upload(self,request):
        if request.method == 'POST':
            videoname = request.POST['videoname']
            videotype = request.POST['videotype']
            filename = request.FILES.get['filename']
            upload = Upload_File(
                videoname=videoname, videotype=videotype, filename=filename,)
            upload.save()
            messages.success(request, "Video Uploaded successfully!")
            return redirect('Project:all media')
        
        return render(request, 'all media.html')

    def form_valid(self, upload):
        upload.save()
        return super(TestUploadView, self).form_valid(upload)


def file(request, id):
    testmodel = get_object_or_404(Upload_File, pk=id)

    return HttpResponse(testmodel.file, content_type='text/plain')

def home(request):
    return render(request, 'index.html')

def MyProject(request):
    return render(request, 'MyProjects.html')

def NewProject(request):
    return render(request, 'newproject.html')

def ResultMyProject(request):
    return render(request, 'ResultMyProject.html')

def All_Media(request):
    return render(request, 'all media.html')
# Create your views here.
