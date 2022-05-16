from urllib import response
from django.test import TestCase
from django.urls import reverse

class SnackTest(TestCase):
    def test_list_page(self):
        url=reverse("snack_List")
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)




    

