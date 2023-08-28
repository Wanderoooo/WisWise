from django.db import models

class Deck(models.Model):
  name = models.CharField(max_length=25)
  description = models.TextField()
  # owner = ForeignKey (to User)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  # is_public = BooleanField (to decide if a deck is shared publicly or is private)
  # category = ForeignKey (to a Category model, if you decide to classify decks)

# class Category(models.Model): ...