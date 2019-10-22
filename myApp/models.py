from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    Image=models.ImageField(upload_to='process_pic/')
