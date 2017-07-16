from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from django.test import TestCase


def assertContents(self, contents):
    for expected_content in contents:
        with self.subTest():
            self.assertContains(self.response, expected_content)


class ProfileViewTest(TestCase):
    """

    """
    def setUp(self):
        user = User.objects.create_user(username='jacob', password='top_secret')
        self.profile = user.profile

        self.client.login(username='jacob', password='top_secret')
        self.response = self.client.get(r(self.profile.get_absolute_url()))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use core/empresa_list.html"""
        self.assertTemplateUsed(self.response, 'accounts/profile_detail.html')

