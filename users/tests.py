from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.
@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple
'''
line 7: The django_user_model fixture is a built-in fixture. It acts as a shortcut to accessing the User model for this project.
line 8-9: This fixture creates a new user with the Django create_user() method and sets a username and password.
line 10: Then it returns the username and password as a tuple
'''

def test_login_user(client, test_user):
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True