from django.test import TestCase
from .models import Computers
from django.contrib.auth import get_user_model
# Create your tests here.


class ComputersTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user3 = get_user_model().objects.create_user(username='joseph3', password='joseph1234')
        user3.save()
        test_computer = Computers.objects.create(modelComputers='laptop3', description='dell', author=user3)
        test_computer.save()

    def test_computers_content(self):
        computer = Computers.objects.get(id=1)
        actual_author = str(computer.author)
        actual_description = str(computer.description)
        self.assertEqual(actual_author, 'joseph3')
        self.assertEqual(actual_description, "dell")
################################################################################################################

