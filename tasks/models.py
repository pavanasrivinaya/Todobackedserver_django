from django.db import models
from utils.models import Timestamps
from django.contrib.auth import get_user_model

# Create your models here.
class Task(Timestamps, models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000,default='', blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title