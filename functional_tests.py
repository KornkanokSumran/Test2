from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000/polls/')
        # She notices the page title and header mention to-do lists
        self.assertIn('polls', self.browser.title)

        # check question 
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('What is your name?', [row.text for row in rows])
        time.sleep(1)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')