from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group


class APIChannelTest(APITestCase):
    fixtures = ['contenttypes.json', 'auth.json', 'channels.json']

    def test_create_channel(self):
        """
        Ensure we can create a new channel object.
        """
        url = reverse('channel-list')
        data = {"name": "AliExpress"}
        user = User.objects.get(username='tester')
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'categories': 'http://testserver/api/channels/aliexpress/categories/', 'url': 'http://testserver/api/channels/aliexpress/', 'name': 'AliExpress'})
