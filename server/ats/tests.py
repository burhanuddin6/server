from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from .models import Users, AccountTypes

class UsersTest(APITestCase):
    def setUp(self):
        # Create a test account type
        self.account_type = AccountTypes.objects.create(account_type='Test')

    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('users-list')
        data = {
            'account_type_id': 1,
            'first_name': 'Test',
            'last_name': 'User',
            'profile_picture': 'http://example.com/profile.jpg',
            'timezone': 'UTC',
        }
        response = self.client.post(url, data, format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 1)
        self.assertEqual(Users.objects.get().first_name, 'Test')
