from django.contrib.auth.models import AbstractUser
from django.db import models


class Subject(models.Model):
    code = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    year = models.IntegerField()


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    subject = models.ManyToManyField(Subject, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']
