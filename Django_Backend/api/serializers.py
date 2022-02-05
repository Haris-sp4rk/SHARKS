from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class userSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class workerSerializer(ModelSerializer):
    class Meta:
        model = worker
        fields = '__all__'

class appointmentSerializer(ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'
    
class feedbackSerializer(ModelSerializer):
    class Meta:
        model = feedback
        fields = '__all__'

class recentSerializer(ModelSerializer):
    class Meta:
        model = recent
        fields = '__all__'

class paymentSerializer(ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'

class ChangePasswordSerializer(serializers.Serializer):
    model = user
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)