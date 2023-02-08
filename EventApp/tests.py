import json

from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class EventPostTest(APITestCase):
    def authenticate(self):
        data_user = {
            "email": "email@gmail.com",
            "username": "username",
            "password": "password"
        }
        user = User.objects.create_user(email=data_user['email'],
                                        username=data_user['username'],
                                        password=data_user['password'])
        user.save()

        endpoint = reverse('auth_default')

        response = self.client.post(endpoint, data_user)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.data['token']}")
        return user

    def test_should_not_create_event_with_no_auth(self):
        data_event = {
            "event_type": "test_event_type",
            "info": {"test_key": "test_value"},
            "timestamp": "2018-11-20T15:58:44.767594-06:00"
        }
        endpoint = reverse('create_event')
        response = self.client.post(endpoint, data_event, format='json')
        json_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_content,
                         {
                             "detail": "Authentication credentials were not provided."
                         })

    def test_should_create_event_with_auth(self):
        self.authenticate()
        data_event = {
            "event_type": "test_event_type",
            "info": {"test_key": "test_value"},
            "timestamp": "2018-11-20T15:58:44.767594-06:00"
        }
        endpoint = reverse('create_event')
        response = self.client.post(endpoint, data_event, format='json')
        json_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_content,
                         {
                             "created": {
                                 "event_type": "test_event_type",
                                 "info": {
                                     "test_key": "test_value"
                                 },
                                 "timestamp": "2018-11-20T15:58:44.767594-06:00"
                             }
                         })
