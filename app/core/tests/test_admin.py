""" Tests for django admin modifications """

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for django admin"""

    # this method allows us to setup some modules at the beginning of different tests
    # that we are going to add in this class, code in setUp will run before every test that we add
    def setUp(self):
        """Create user and client"""
        self.client = Client()  # django test client which allows to make http requests
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_list(self):
        "Test that users are listed on page"
        # this syntax determines which URL we are going to pull from django admin
        url = reverse('admin:core_user_changelist')
        # make the http request to url to get list of users
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_users_page(self):
        "Test that edit user page works"
        # this syntax determines which URL we are going to pull from django admin
        url = reverse('admin:core_user_change', args=[self.user.id])
        # make the http request to url to get list of users
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page_works(self):
        """Test create user page"""
        # this syntax determines which URL we are going to pull from django admin
        url = reverse('admin:core_user_add')
        # make the http request to url to get list of users
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
