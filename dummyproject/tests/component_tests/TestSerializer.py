import unittest, io
from rest_framework.parsers import JSONParser
from dummyproject import serializers

def json_to_serializer(json_bytes):
    stream = io.BytesIO(json_bytes)
    data = JSONParser().parse(stream)

    return serializers.PersonSerizlizer(data=data)

class TestSerializer(unittest.TestCase):
    def test_validate_does_not_fail_with_valid_data(self):
        json_bytes = b'{"name":"staiksi", "email": "astaykov@student.fontys.nl", "age": 21, "cool": true, "amount_of_coolness": 99.99,"date_of_coolness": "2016-01-27 15:17:10.375877"}'

        self.assertTrue(json_to_serializer(json_bytes).is_valid())

    def test_validate_fails_with_invalid_name(self):
        json_bytes = b'{"name":"as", "email": "astaykov@student.fontys.nl", "age": 21, "cool": true, "amount_of_coolness": 99.99,"date_of_coolness": "2016-01-27 15:17:10.375877"}'

        self.assertFalse(json_to_serializer(json_bytes).is_valid())
