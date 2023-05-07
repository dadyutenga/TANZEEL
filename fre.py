from django.db import models
from django.contrib.auth.models import User

class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    document = models.FileField(upload_to='documents/', blank=True)
    picture = models.ImageField(upload_to='pictures/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
