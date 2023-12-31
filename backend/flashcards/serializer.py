from rest_framework import serializers
from .models import *

class FlashcardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Flashcard
    fields = ['deck', 'question', 'answer']