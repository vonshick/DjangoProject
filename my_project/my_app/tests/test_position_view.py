from django.test import TestCase
from django.test import Client
from django.urls import reverse

from my_app.models import Position

from django.contrib.auth.models import User


class PositionViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('John', 'john@example.com', 'password')
        Position.objects.create(name='Pos1', min_salary=5, max_salary=10)

    def test_get_all_positions(self):
        client = Client()

        client.login(username='John', password='password')
        response = client.get(reverse('all_positions'))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['object_list'][0].name, 'Pos1')

