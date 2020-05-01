from datetime import datetime, timezone
from django.test import TestCase
from dummyproject.models import Person
from rest_framework.test import APIClient

class TestPersonEdpoints(TestCase):

    def setUp(self):
        self.client = APIClient()
    
    def test_get_user(self):
        Person.objects.create(
            name = 'staiksi',
            age = 21,
            cool = True,
            amount_of_coolness = 99.99,
            email = "astaykov@student.fontys.nl",
            date_of_coolness = datetime.now(tz=timezone.utc)
        )   
        
        response = self.client.get('/api/person/1/')

        self.assertContains(response, '"name":"staiksi"')
