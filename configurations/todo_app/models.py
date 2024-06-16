from django.db import models
from django.contrib.auth import get_user_model

class Note(models.Model):
    title=models.CharField(max_length=56,null=False)
    note=models.TextField(max_length=500)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
