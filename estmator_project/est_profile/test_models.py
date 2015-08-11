from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase

from estmator_project.factories import UserFactory
from .models import UserProfile


class UserProfileTestCase(TestCase):
    """Test behavior of user profile"""
    def setUp(self):
        pass

    def tearDown(self):
        User.objects.all().delete()

    def test_profile_is_created_when_user_is_saved(self):
        self.assertEqual(len(UserProfile.objects.all()), 0)
        user = UserFactory.create()
        user.save()
        self.assertTrue(UserProfile.objects.count() == 1)

    def test_delete_profile_deletes_user(self):
        user = UserFactory.create()
        user.save()
        self.assertEqual(len(UserProfile.objects.all()), 1)
        user.profile.delete()
        self.assertEqual(len(User.objects.all()), 0)

    def test_profile_str_is_user_username(self):
        user = UserFactory.create(username='user1')
        user.save()
        profile = UserProfile.objects.get(user__username='user1')
        self.assertEqual(str(profile),
                         user.get_full_name() or profile.user.username)
