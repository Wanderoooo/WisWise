from rest_framework import serializers
from .models import *

class StudySessionSerializer(serializers.ModelSerializer):
  class Meta:
    model = StudySession
    fields = ['user', 'started_at', 'ended_at']