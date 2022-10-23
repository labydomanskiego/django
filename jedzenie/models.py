from django.db import models
# Create your models here.

class Jedzenie(models.Model):
    danie = models.CharField(max_length=100)
    kcal = models.IntegerField()
    smaczne = models.BooleanField()
    create_time = models.DateTimeField('create time')
    last_edit_time = models.DateTimeField('last edit time')