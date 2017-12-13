from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class sp(models.Model):
	name = models.CharField(max_length=20, unique=True)
	super_power = models.CharField(max_length=500)
	date = models.DateTimeField(default=datetime.now,blank =True)
	display_image = models.ImageField(upload_to="display_picture/")


def __str__(self):
		return self.name

class Meta:
	verbose_name_plural = "sp"
