from django.db import models


class Subject(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    year = models.IntegerField()

    # EJEMPLO: {"code": 2000, "name": "FISICA", "credits": 7, "year": 2019}
