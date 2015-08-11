from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase

from estmator_project.factories import UserFactory
from .models import UserProfile


class UserProfileTestCase(TestCase):
    """Test behavior of user profile"""
    def setUp(self):
        pass
        
