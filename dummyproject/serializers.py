from rest_framework import serializers

from dummyproject.models import Person

class PersonSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'