from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question,default=1, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class dummy(models.Model):
    question = models.ForeignKey(Question,default=1,on_delete=models.CASCADE)
    dummy_char= models.CharField(max_length=200)
    date = models.DateTimeField(null=True)
    title = models.CharField(blank=True,max_length=25)

    def __str__(self):
        return self.dummy_char