from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class userSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

