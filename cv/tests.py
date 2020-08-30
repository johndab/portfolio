from django.urls import resolve
from django.test import TestCase
from .views import cv
from django.http import HttpRequest

class CvPageTest(TestCase):

    def test_view_returns_cv(self):
        found = resolve('/cv')  
        self.assertEqual(found.func, cv)

    # def test_view_returns_sections(self):
    #     request = HttpRequest()  
    #     response = cv(request)
        # self.assertEqual(found.func, cv)
