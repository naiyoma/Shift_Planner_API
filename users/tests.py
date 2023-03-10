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
        self.url = '/api/createuser/'
        self.shift_url = '/api/create_shift/'
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


    def test_create_custom_user_without_email(self):
        """
        Test Invalid data on User.
        """
        self.user_data['email'] = ''
        response = self.client.post(self.url, self.user_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_filter_shifts_by_user(self):
        """
        Test that a user can filter shifts based on ID.
        """
        self.user = CustomUser.objects.create(
            username='test_user',
            password='12345',
            email='test@example.com',
            is_staff=True,
            department='Product',
            position='Developer'
        )
        self.shift = UserShift.objects.create(
            user=self.user,
            date='2022-09-09',
            shift='08:00:00-16:00:00',
            title='Test Shift',
            description='This is a test shift'
        )
        user_id = self.user.id
        response = self.client.get(f'/api/shifts/{user_id}/')
        self.assertEqual(response.status_code, 200)
