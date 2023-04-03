import datetime

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    objects = models.Manager()


class Question(BaseModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1)).timestamp()


class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
