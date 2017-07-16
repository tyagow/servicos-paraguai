from django.contrib.auth.models import User
from django.shortcuts import resolve_url
from django.test import TestCase

from src.accounts.models import Profile


def assertContents(self, contents):
    for expected_content in contents:
        with self.subTest():
            self.assertContains(self.response, expected_content)


class ProfileModelTest(TestCase):
    """    """
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', password='top_secret')
        self.profile = self.user.profile

    def test_create(self):
        self.assertTrue(Profile.objects.exists())

    def test_str(self):
        self.assertEqual(self.profile.user.username, str(self.profile))

    def test_get_absolute_url(self):
        url = resolve_url('user_profile', slug=self.profile.slug)
        self.assertEqual(url, self.profile.get_absolute_url())



