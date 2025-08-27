from django.db import models


class Calculate(models.Model):
    number_1 = models.CharField(max_length=15),
    number_2 = models.CharField(max_length=15),
    sign = models.CharField(max_length=15)