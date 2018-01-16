from django.db import models

# Create your models here.
class Add_Word(models.Model):
    word_text = models.CharField(max_length = 140)
    date_time = models.DateTimeField('保存日')
