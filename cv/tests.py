from django.urls import resolve
from django.test import TestCase
from .views import cv
from django.http import HttpRequest

class CvPageTest(TestCase):

    def test_view_returns_cv(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html')

    def test_cv_form_page_returns_correct_html(self):
        response = self.client.get('/cv/new')
        self.assertTemplateUsed(response, 'cv/form.html')