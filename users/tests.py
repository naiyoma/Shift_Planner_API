from django.test import TestCase
from rest_framework.test import APIClient
from .models import CustomUser
from .serializers import CustomeRegisterSerializer

# Create your tests here.

class CustomerUserViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/customer_users/'
        self.user_data = {
            'username': 'MOna',
            'password': '12345',
            'is_staff': True,
            'department': 'Product',
            'position': 'Developer'
        }
        self.response = self.client.post(self.url, self.user_data)
    
    
    def test_create_user_without_email(self):
        self.user_data['email'] = ''
        response = self.client.post(self.url, self.user_data)
        self.assertEqual(response.status_code, 400)