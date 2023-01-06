import uuid
from datetime import date
from django.test import TestCase
from django.db import IntegrityError
from rest_framework.test import APIClient
from .models import CustomUser, UserShift
from .serializers import CustomeRegisterSerializer

# Create your tests here.

class UserShiftViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/createuser/'
        self.shift_url = '/create_shift/'
        self.user_data = {
            'id': str(uuid.uuid4()),
            'username': 'MonaLisa',
            'password': '12345',
            'email': 'Tiana@gmail.com',
            'department': 'Product',
            'position': 'Developer'
        }
        self.user_response = self.client.post(self.url, self.user_data)
        self.user_id = self.user_response.data['id']
        self.shift_data = {
            'user': self.user_id,
            'date' : '2029-03-01',
            'shift': '08:00:00-16:00:00',
            'title': 'ServiceTest',
            'description': '123456'
        }

        self.client.post(self.shift_url, self.shift_data)
        
    def test_create_a_user_shift(self):
        """
        Test creation of a shift with valid data.
        """
        self.shift_data = {
            'user': self.user_id,
            'date' : '2028-03-01',
            'shift': '08:00:00-16:00:00',
            'title': 'ServiceTest',
            'description': '123456'
        }
       
        shift_response = self.client.post(self.shift_url, self.shift_data)
        self.assertEqual(shift_response.status_code, 201)
        
    def test_user_and_date_are_unique_together(self):
        """
        A worker never has two shifts on the same day.
        """
        self.shift_data1 = {
            'user': self.user_id,
            'date' : '2029-03-01',
            'shift': '08:00:00-16:00:00',
            'title': 'ProductV1',
            'description': 'meetings'
        }
        shift_response1 = self.client.post(self.shift_url, self.shift_data1)
        self.assertEqual(shift_response1.status_code, 400)


