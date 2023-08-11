from django.db import models

# Create your models here.
class ANSWER_CHOICES(models.TextChoices): 
    StronglyAgree = 'Strongly Agree', ('Strongly Agree')
    Agree = 'Agree', ('Agree')
    NeitherAgreeorDisagree = 'Neither Agree or Disagree', ('Neither Agree or Disagree')
    Disagree = 'Disagree', ('Disagree')
    StronglyDisagree = 'Strongly Disagree', ('Strongly Disagree')

class Survey(models.Model):
    Q1 = models.CharField(max_length=25, choices=ANSWER_CHOICES.choices, default=ANSWER_CHOICES.NeitherAgreeorDisagree)
    Q2 = models.CharField(max_length=25, choices=ANSWER_CHOICES.choices, default=ANSWER_CHOICES.NeitherAgreeorDisagree)
    Q3 = models.CharField(max_length=25, choices=ANSWER_CHOICES.choices, default=ANSWER_CHOICES.NeitherAgreeorDisagree)
    
    class Meta:
        ordering = ['Q1', 'Q2', 'Q3']
    
    def __str__(self):
        return f'{self.Q1}, {self.Q2}, {self.Q3}'