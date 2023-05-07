from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from .models import Contribution

@staff_member_required
@require_GET
def download_file(request, pk, field_name):
    contribution = get_object_or_404(Contribution, pk=pk)
    field = getattr(contribution, field_name)
    response = HttpResponse(field.read(), content_type=field.content_type)
    response['Content-Disposition'] = f'attachment; filename="{field.name}"'
    return response
