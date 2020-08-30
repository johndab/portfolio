from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from django.test import LiveServerTestCase
import unittest

class CvVisitorTest(LiveServerTestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_enter_cv(self):
        # Jan can see a home page
        self.browser.get(self.live_server_url)
        self.assertIn('Jan\'s blog', self.browser.title)

        navbar = self.browser.find_element_by_id("navbarResponsive")
        links = navbar.find_elements_by_tag_name('a')
        self.assertEqual(2, len(links))
        links[1].click()

        self.assertIn('Jan\'s CV', self.browser.title)

        navbar = self.browser.find_element_by_id("navbarResponsive")
        links = navbar.find_elements_by_tag_name('a')
        self.assertEqual(2, len(links))
        links[0].click()

        self.assertIn('Jan\'s blog', self.browser.title)


    def test_can_see_cv(self):
        # Jan accesses a CV subpage
        self.browser.get(self.live_server_url + '/cv')

        # He notices the page header mention cv
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Jan Dabrowski', header_text)

        # He can see different sections
        section_ids = ['professionalExperience', 'freelance', 'technologies', 'education', 'languages', 'hobbies']
        section_titles = ['Professional Experience', 'Freelance Jobs', 'Technologies' ,'Education', 'Languages', 'Hobbies']

        for id, title in zip(section_ids, section_titles):
            section = self.browser.find_element_by_xpath("//div[@id='{0}']".format(id))
            section_title = section.find_element_by_tag_name("h2").text
            self.assertIn(title, section_title)

    def test_can_add_cv_section(self):
        self.browser.get(self.live_server_url + '/cv/new')
        form = self.browser.find_element_by_tag_name('form')
        
        # Select CV section
        select_section = Select(form.find_element_by_name('section'))
        select_section.select_by_visible_text('Professional Experience')
        
        # Provide title
        title_element = form.find_element_by_name("title")
        title_element.send_keys("Test title")

        # Provide date
        date_element = form.find_element_by_name("date")
        date_element.send_keys("05/2020")

        # Provide subtitle
        subtitle_element = form.find_element_by_name("subtitle")
        subtitle_element.send_keys("Test subtitle 123")

        # Provide content
        content_element = form.find_element_by_name("content")
        content_element.send_keys("Bla bla content bla bla")

        self.browser.find_element_by_id("submit").click()

        # The form redirects back to the cv
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Jan Dabrowski', header_text)

        section = self.browser.find_element_by_xpath("//div[@id='professionalExperience']")
        section_items = section.find_elements_by_class_name('item')
        self.assertEqual(1, len(section_items))
