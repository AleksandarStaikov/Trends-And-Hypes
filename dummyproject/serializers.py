from rest_framework import serializers

from dummyproject.models import Person
from dummyproject.validators import (
    validate_age,
    validate_amount_of_coolness, 
    validate_date_of_coolness,
    validate_email,
    validate_name
)

class PersonSerizlizer(serializers.ModelSerializer):
    def validate(self, data):
        import pdb; pdb.set_trace()
        validate_name(data['name'])
        validate_age(data['age'])
        validate_email(data['email'])
        validate_date_of_coolness(data['date_of_coolness'])
        validate_amount_of_coolness(data['amount_of_coolness'])
        
        return data

    class Meta:
        model = Person
        fields = '__all__'