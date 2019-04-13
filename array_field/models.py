from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Sentence(models.Model):
    sent = models.CharField(max_length=150)
    msg_list = ArrayField(models.CharField(max_length=500), blank=True)
    sent_correct = models.CharField(max_length=300, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
