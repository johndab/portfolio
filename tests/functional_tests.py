from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_enter_cv(self):
        # Jan can see a home page
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Jan\'s blog', self.browser.title)

        navbar = self.browser.find_element_by_id("navbarResponsive")
        links = navbar.find_elements_by_tag_name('a')
        self.assertEqual(2, len(links))
        links[1].click()

        self.assertIn('Jan\'s CV', self.browser.title)


    def test_can_see_cv(self):
        # Jan accesses a CV subpage
        self.browser.get('http://127.0.0.1:8000/cv')

        # He notices the page header mention cv
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Jan\'s CV', header_text)

        # He can see different sections
        section_ids = ['professionalExperience', 'freelance', 'technologies', 'education', 'languages', 'hobbies']
        section_titles = ['Professional experience', 'Freelance Jobs', 'Technologies' ,'Education', 'Languages', 'Hobbies']

        for id, title in zip(section_ids, section_titles):
            section_title = self.browser.find_element_by_xpath("//div[@id='{0}']/h1".format(section_id)).text
            self.assertIn(title, section_title)
            section_items = self.browser.find_elements_by_xpath("//div[@id='{0}']/items/div".format(section_id))
            # has children
            self.assertGreater(len(section_items), 0)

if __name__ == '__main__':  
    unittest.main() 
