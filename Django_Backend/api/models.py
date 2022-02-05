from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.reverse_related import ManyToOneRel
from django.dispatch import receiver
from django.urls import reverse
import datetime
import os

# Create your models here.

class user(models.Model):
    username = models.TextField(unique=True,primary_key=True)
    password = models.TextField(null=False)
    

