import uuid
from django.test import TestCase
from rest_framework.test import APIClient
from .models import CustomUser
from datetime import datetime
from .serializers import CustomeRegisterSerializer

# Create your tests here.


# class CustomerUserViewSetTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.url = '/createuser/'
#         self.user_data = {
#             'id': str(uuid.uuid4()),
#             'username': 'MOna',
#             'password': '12345',
#             'email': 'lankas.aurelia@gmail.com',
#             'is_staff': True,
#             'department': 'Product',
#             'position': 'Developer'
#         }
#         self.response = self.client.post(self.url, self.user_data)
#         self.user_id = self.response.data['id']
    
#     def test_create_user_without_username(self):
#         """
#         Testing for invalid data on user model.
#         """
#         self.user_data['username'] = ""
#         response = self.client.post(self.url, self.user_data)
#         self.assertEqual(response.status_code, 400)
#         self.assertEqual(CustomUser.objects.count(), 0)

#test that a user can create a shift with valid and invalid data.
#test that a user can not have more than shift.
class UserShiftViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/createuser/'
        self.shift_url = '/create_shift/'
        self.user_data = {
            'id': str(uuid.uuid4()),
            'username': 'MOna',
            'password': '12345',
            'email': 'lankas.aurelia@gmail.com',
            'is_staff': True,
            'department': 'Product',
            'position': 'Developer'
        }
        self.user_response = self.client.post(self.url, self.user_data)
        self.user_id = self.user_response.data['id']
        self.shift_data = {
            'user': self.user_id,
            # 'date': datetime.now().strftime('%Y-%m-%d'),
            'date' : '2022-09-09',
            'shift': '08:00:00-16:00:00',
            'title': 'ServiceTest',
            'description': '123456'
        }

        self.shift_response = self.client.post(self.shift_url, self.shift_data)
        
    
    def test_create_a_user_shift(self):
        import pdb; pdb.set_trace()
        """
        Test creation of a shift with valid data.
        """
        response = self.client.post(self.shift_url, self.shift_data)
        self.assertEqual(response.status_code, 200)
