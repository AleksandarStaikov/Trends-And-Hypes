import unittest
from datetime import datetime, timedelta
from dummyproject import validators
from rest_framework import serializers 

class TestValidators(unittest.TestCase):
    def setUp(self):
        self.username_validation_error = 'Name should be between 3 and 50 symbols!'
        self.age_validation_error = 'Sorry we do not accept babies and boomers!'
        self.email_validation_error = 'Only Fontys students are accepted, duck off!'
        self.date_of_coolness_validation_error = 'You cant predict is you are gonna become cool in the furue duh!'
        self.amount_of_coolness_validation_error = 'Coolness amount must be between 0 and 100!'

    def tearDown(self):
        #define tear down logic
        pass

    def test_username_too_short_validation(self):
        with self.assertRaisesRegex(serializers.ValidationError, self.username_validation_error):
            validators.validate_name('aa')

    def test_username_too_long_validation(self):
        with self.assertRaisesRegex(serializers.ValidationError, self.username_validation_error):
            validators.validate_name('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    def test_username_boundary_validation_should_not_fail(self):
        try:
            validators.validate_name('aaa')
            validators.validate_name('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        except:
            self.fail('Unexpected exception')


    def test_foreign_email_should_throw(self):
        with self.assertRaisesRegex(serializers.ValidationError, self.email_validation_error):
            validators.validate_email('astaykov@not.fontys.nl')

    def test_fontys_email_should_not_throw(self):
        try:
            validators.validate_email('astaykov@student.fontys.nl')
        except:
            self.fail('Unexpected exception')


    def test_age_too_young_validation(self):
        with self.assertRaisesRegex(serializers.ValidationError, self.age_validation_error):
            validators.validate_age(14)

    def test_age_too_old_validation(self):
        with self.assertRaisesRegex(serializers.ValidationError, self.age_validation_error):
            validators.validate_age(31)

    def test_age_boundary_validation_should_not_fail(self):
        try:
            validators.validate_age(15)
            validators.validate_age(30)
        except:
            self.fail('Unexpected exception')


    def test_date_of_coolness_in_the_future_validation(self):
        with self.assertRaisesRegex(serializers.ValidationError, self.date_of_coolness_validation_error):
            validators.validate_date_of_coolness(datetime.now() + timedelta(hours=1))

    def test_date_of_coolness_boundary_validation_should_not_fail(self):
        try:
            validators.validate_date_of_coolness(datetime.now())
        except:
            self.fail('Unexpected exception')


    def test_negative_amount_of_coolness_validation(self):
        with self.assertRaisesRegex(serializers.ValidationError, self.amount_of_coolness_validation_error):
            validators.validate_amount_of_coolness(-1)

    def test_too_high_amount_of_coolness_validation(self):
        with self.assertRaisesRegex(serializers.ValidationError, self.amount_of_coolness_validation_error):
            validators.validate_amount_of_coolness(100.01)

    def test_amount_of_coolness_boundary_validation_should_not_fail(self):
        try:
            validators.validate_amount_of_coolness(0)
            validators.validate_amount_of_coolness(100)
        except:
            self.fail('Unexpected exception')