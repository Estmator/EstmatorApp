from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Company(models.Model):
    company_name = models.CharField(max_length=256)
    phone = models.IntegerField()
    address = models.CharField(max_length=256)
    address2 = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    postal = models.IntegerField()

    def __str__(self):
        return self.company_name


@python_2_unicode_compatible
class Client(models.Model):
    company = models.ForeignKey(Company)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    cell = models.IntegerField()
    desk = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name
