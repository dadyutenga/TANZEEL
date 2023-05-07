from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Contribution

class ContributionCreateView(CreateView):
    model = Contribution
    fields = ['amount', 'description', 'document', 'picture']
    success_url = reverse_lazy('contributions_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
