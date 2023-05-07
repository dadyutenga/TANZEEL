from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import UploadedFile

class UploadFileView(CreateView):
    model = UploadedFile
    fields = ['file', 'description']
    success_url = reverse_lazy('file_list')
    
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
