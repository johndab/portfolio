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

        navbar = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "menu"))
        )

        links = navbar.find_elements_by_tag_name('a')
        self.assertEqual(2, len(links))
        links[1].click()

        self.assertIn('Jan\'s CV', self.browser.title)

        navbar = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "menu"))
        )
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
        section_ids = ['professionalExperience', 'technologies', 'education', 'languages', 'hobbies']
        section_titles = ['Professional Experience', 'Technologies', 'Education', 'Languages', 'Hobbies']

        for id, title in zip(section_ids, section_titles):
            section = self.browser.find_element_by_xpath("//div[@id='{0}']".format(id))
            section_title = section.find_element_by_tag_name("h2").text
            self.assertIn(title, section_title)

    # Helper function for filling the form
    def fill_form(self, section, title, subtitle, date, content):
        form = self.browser.find_element_by_tag_name('form')
        
        # Select CV section
        select_section = Select(form.find_element_by_name('section'))
        select_section.select_by_visible_text(section)
        
        # Provide title
        title_element = form.find_element_by_name("title")
        title_element.send_keys(title)

        # Provide date
        date_element = form.find_element_by_name("date")
        date_element.send_keys(date)

        # Provide subtitle
        subtitle_element = form.find_element_by_name("subtitle")
        subtitle_element.send_keys(subtitle)

        # Provide content
        content_element = form.find_element_by_name("content")
        content_element.send_keys(content)

        self.browser.find_element_by_id("submit").click()


    def test_can_add_cv_prof_experience(self):
        self.browser.get(self.live_server_url + '/cv/new')

        self.fill_form(
            'Professional Experience', 
            "Test title", 
            "Test subtitle 123", 
            "05/2020", 
            "Bla bla content bla bla"
        )

        # The form redirects back to the cv
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Jan Dabrowski', header_text)

        section = self.browser.find_element_by_xpath("//div[@id='professionalExperience']")
        section_items = section.find_elements_by_class_name('item')
        self.assertEqual(1, len(section_items))

        item = section_items[0]
        title = item.find_element_by_class_name("title").text
        self.assertIn("Test title", title)

        subtitle = item.find_element_by_class_name("subtitle").text
        self.assertIn("Test subtitle 123", subtitle)

        date = item.find_element_by_class_name("date").text
        self.assertIn("05/2020", date)

        content = item.find_element_by_class_name("content").text
        self.assertIn("Bla bla content bla bla", content)

    def test_can_add_cv_education(self):
        self.browser.get(self.live_server_url + '/cv/new')

        self.fill_form(
            "Education", 
            "Uni of Bham", 
            "", 
            "05/2017", 
            "Uni content bla bla"
        )

        # The form redirects back to the cv
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Jan Dabrowski', header_text)

        section = self.browser.find_element_by_xpath("//div[@id='education']")
        section_items = section.find_elements_by_class_name('item')
        self.assertEqual(1, len(section_items))

        item = section_items[0]
        title = item.find_element_by_class_name("title").text
        self.assertIn("Uni of Bham", title)

        date = item.find_element_by_class_name("date").text
        self.assertIn("05/2017", date)

        content = item.find_element_by_class_name("content").text
        self.assertIn("Uni content bla bla", content)


    def test_can_add_cv_technologies(self):
        self.browser.get(self.live_server_url + '/cv/new')

        self.fill_form(
            "Technologies", 
            "C#", 
            "", 
            "", 
            ".NET Core"
        )

        # The form redirects back to the cv
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Jan Dabrowski', header_text)

        section = self.browser.find_element_by_xpath("//div[@id='technologies']")
        section_items = section.find_elements_by_class_name('item')
        self.assertEqual(1, len(section_items))

        item = section_items[0]
        title = item.find_element_by_class_name("title").text
        self.assertIn("C#", title)

        content = item.find_element_by_class_name("content").text
        self.assertIn(".NET Core", content)


    def test_can_add_cv_languages(self):
        self.browser.get(self.live_server_url + '/cv/new')

        self.fill_form(
            "Languages", 
            "English", 
            "", 
            "", 
            "Fluent"
        )

        # The form redirects back to the cv
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Jan Dabrowski', header_text)

        section = self.browser.find_element_by_xpath("//div[@id='languages']")
        section_items = section.find_elements_by_class_name('item')
        self.assertEqual(1, len(section_items))

        item = section_items[0]
        title = item.find_element_by_class_name("title").text
        self.assertIn("English", title)

        content = item.find_element_by_class_name("content").text
        self.assertIn("Fluent", content)


    def test_can_add_cv_hobbies(self):
        self.browser.get(self.live_server_url + '/cv/new')

        self.fill_form(
            "Hobbies", 
            "Running", 
            "", 
            "", 
            "Trainings"
        )

        # The form redirects back to the cv
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Jan Dabrowski', header_text)

        section = self.browser.find_element_by_xpath("//div[@id='hobbies']")
        section_items = section.find_elements_by_class_name('item')
        self.assertEqual(1, len(section_items))

        item = section_items[0]
        title = item.find_element_by_class_name("title").text
        self.assertIn("Running", title)

        content = item.find_element_by_class_name("content").text
        self.assertIn("Trainings", content)