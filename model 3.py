from django.views.generic.list import ListView
from .models import UploadedFile

class FileListView(ListView):
    model = UploadedFile
    template_name = 'file_list.html'
    
    def get_queryset(self):
        return UploadedFile.objects.filter(uploaded_by=self.request.user)
