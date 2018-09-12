from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=50)
    disease = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pin_code = models.CharField(max_length=50)

    def __unicode__(self):
        return self.email.first_name

class MedicineUserData(models.Model):
    user_id = models.ForeignKey(UserInfo)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    course_time = models.DateField()
    daily_dosage = models.IntegerField()
    reminder = models.CharField(max_length=20, null=True)



    def __unicode__(self):
        return self.user_id.email.username