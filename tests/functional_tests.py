from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_is_app_online(self):  
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Jan\'s blog', self.browser.title)  


if __name__ == '__main__':  
    unittest.main() 
