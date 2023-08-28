from django.db import models

class StudySession(models.Model):
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  # deck(s) = ManytoMany? (to Deck)
  started_at = models.DateTimeField(auto_now_add=True) # created @ study start
  ended_at = models.DateTimeField(auto_now=True) # modified when study session ends
  # total_cards = models.IntegerField(), similar to deck
  # correct_answers = models.IntegerField(), implement later w/ cards/deck
  

# FlashcardHistory (track how a user interacts with a specific card over time):

# flashcard: ForeignKey (to Flashcard)
# user: ForeignKey (to User)
# viewed_at: DateTimeField
# was_correct: BooleanField (whether the user answered correctly in the session)