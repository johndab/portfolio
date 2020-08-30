from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n<!doctype html>'))  
        self.assertIn('<title>Jan\'s blog</title>', html)  
        self.assertTrue(html.endswith('</html>'))