from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class UserLoginTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(username='testuser', email='test@example.com',
                                                  password='testpassword')

    def test_user_login_with_valid_credentials(self):
        # Create a test client
        client = APIClient()

        # Authenticate the client
        client.login(username='testuser', password='testpassword')

        # Make a POST request to the user_login endpoint with valid credentials
        url = reverse('user_login')
        response = client.post(url, {'username': 'testuser', 'password': 'testpassword'})

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains the expected data
        self.assertIn('token', response.data)

    def test_user_login_with_invalid_credentials(self):
        # Create a test client
        client = APIClient()

        # Make a POST request to the user_login endpoint with invalid credentials
        url = reverse('user_login')
        response = client.post(url, {'username': 'testuser', 'password': 'wrongpassword'})

        # Assert that the response status code is 400
        self.assertEqual(response.status_code, 400)

        # Assert that the response contains the expected error message
        self.assertEqual(response.data, {'error': 'Invalid credentials.'})

    # def test_user_signup(self):
    #     # Create a test client
    #     client = APIClient()
    #
    #     # Make a POST request to the user_signup endpoint with the necessary data
    #     url = reverse('user_signup')
    #     response = client.post(url, {'username': 'testuser', 'password': 'testpassword'})
    #
    #     # Assert that the response status code is 201
    #     self.assertEqual(response.status_code, 201)
    #
    #     # Assert that a new user is created in the database
    #     self.assertTrue(User.objects.filter(username='testuser').exists())
    #
    #     # Assert that the response contains the expected data
    #     self.assertIn('id', response.data)
    #     self.assertEqual(response.data['username'], 'testuser')
