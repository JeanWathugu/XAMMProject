from django.db import models

class learners (models.Model):
    lid = models.IntegerField(max_length=10)
    lname = models.CharField(max_length= 60)
    lage = models.IntegerField(max_length=3)
    lemail = models.EmailField()
    lcontact = models.IntegerField(max_length=11)

class Meta:
    db_table = "learners"


# Create your models here.
