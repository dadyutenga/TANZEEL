from django.urls import path
from .views import all_contributions

urlpatterns = [
    # ...
    path('contributions/all/', all_contributions, name='all_contributions'),
    # ...
]
