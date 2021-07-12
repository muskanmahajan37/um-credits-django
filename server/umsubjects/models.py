from django.db import models


class Subject(models.Model):
    code = models.IntegerField(max_length=4, unique=True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField(max_length=1)
    year = models.IntegerField(max_length=4)

    # EJEMPLO: {"code": 2000, "name": "FISICA", "credits": 7, "year": 2019}
