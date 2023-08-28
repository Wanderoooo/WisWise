from rest_framework import serializers
from .models import *

class DeckSerializer(serializers.ModelSerializer):
  class Meta:
    model = Deck
    fields = ['name', 'description', 'created_at', 'modified_at']