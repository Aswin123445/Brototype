from django.db import models as db

# Create your models here.
class Member(db.Model):
    first_name=db.CharField(max_length=200)
    second_name=db.CharField(max_length=200)

