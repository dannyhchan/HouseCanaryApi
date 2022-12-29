from django.db import models

# Create your models here.
class AnswerModel(models.Model):
    id = models.IntegerField(primary_key=True)
    questionId = models.IntegerField()
    answer = models.CharField(max_length=200)
    propertyId = models.IntegerField()
    
    def __str__(self):
        return self.answer