from rest_framework import validators, serializers

from datetime import datetime

def validate_name(value):
    if 3 > len(value) or len(value) > 50:
        raise serializers.ValidationError('Name should be between 3 and 50 symbols!')

def validate_email(value):
    if not value.endswith('@student.fontys.nl'):
        raise serializers.ValidationError('Only Fontys students are accepted, duck off!')

def validate_amount_of_coolness(value):
    if 0 > value or value > 100:
        raise serializers.ValidationError('Coolness amount must be between 0 and 100!')

def validate_date_of_coolness(value):
    if value > datetime.now():
        raise serializers.ValidationError('You cant predict is you are gonna become cool in the furue duh!')

def validate_age(value):
    if 15 > value or value > 30:
        raise serializers.ValidationError('Sorry we do not accept babies and boomers!')