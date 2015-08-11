from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
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
    cell = models.CharField(max_length=20)
    desk = models.CharField(max_length=20,
                            blank=True)

    objects = models.Manager()
    active = ActiveProfileManager()

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    @property
    def is_active(self):
        return self.user.is_active
