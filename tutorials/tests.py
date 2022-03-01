from django.test import TestCase
from django.urls import reverse
from tutorials.models import Tutorial
import pytest

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"
    
@pytest.fixture 
def new_tutorial(db): # unction will create a new tutorial object with the attributes described (a title of 'Pytest', etc) any time it is used as a parameter in a test function. db is a built-in fixture provided by pytest django
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# These test functions use new_tutorial as a parameter

def test_search_tutorials(new_tutorial): # simply checks that the object created by the fixture exists, by searching for an object with the same title.
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial): # updates the title of the new_tutorial object, saves the update, and asserts that a tutorial with the updated name exists in the database. 
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()
    
@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk

'''
line 41: Both the objects returned from the new_tutorial and another_tutorial fixtures are passed in
line 42: Then, the test asserts that the .pk attributes are not equal to the other. The .pk attribute in the Django ORM refers to the primary key of a database object, which is automatically generated when it is created.
'''
