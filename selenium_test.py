import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WebResumeSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_home(self):
        browser = self.browser
        browser.get("http://204.209.76.218:8000/")

        contact = browser.find_element_by_id("contact")
        about = browser.find_element_by_id("about")
        education = browser.find_element_by_id("education")
        skills = browser.find_element_by_id("skills")
        work = browser.find_element_by_id("work")
        name = browser.find_element_by_id("name")

        assert browser.find_element_by_id("contact") != None
        assert browser.find_element_by_id("about") != None
        assert browser.find_element_by_id("education") != None
        assert browser.find_element_by_id("skills") != None
        assert browser.find_element_by_id("work") != None
        assert browser.find_element_by_id("name") != None

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()

