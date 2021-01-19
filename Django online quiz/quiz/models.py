from django.db import models


# Create your models here.


class Quiz(models.Model):
    question = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100)
    choice4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question
