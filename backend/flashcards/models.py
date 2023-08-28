from django.db import models

class Flashcard(models.Model):
  deck = models.ForeignKey('Deck', on_delete=models.CASCADE)
  question = models.TextField()
  answer = models.TextField()
  # hint = TextField (optional)
  # created_at = DateTimeField
  # updated_at = DateTimeField
  # image = ImageField (optional, if you want to associate images with flashcards)
  # audio = FileField (optional, for pronunciation or other audio clips)
