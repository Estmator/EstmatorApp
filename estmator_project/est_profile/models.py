from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.forms import (
    USPhoneNumber,
    USStateSelect,
    USZipCodeField
)
from django.utils.encoding import python_2_unicode_compatible


class ActiveProfileManager(models.Manager):
    def get_queryset(self):
        return super(ActiveProfileManager, self).get_queryset()\
            .filter(user__is_active=True)


@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        null=False
    )
    cell = USPhoneNumber()
    desk = USPhoneNumber()

    objects = models.Manager()
    active = ActiveProfileManager()

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    @property
    def is_active(self):
        return self.user.is_active


@python_2_unicode_compatible
class Company(models.Model):
    company_name = models.CharField()
    phone = USPhoneNumber()
    address = models.CharField()
    address2 = models.CharField()
    city = models.CharField()
    state = USStateSelect()
    postal = USZipCodeField()


@python_2_unicode_compatible
class Client(models.Model):
    company = models.OneToOneField(
        Company,
        related_name='company')
    first_name = models.CharField()
    last_name = models.CharField()
    title = models.CharField()
    cell = USPhoneNumber()
    desk = USPhoneNumber()
    email = models.EmailField()
