from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
    browser = webdriver.Firefox(executable_path="C:\\gecko_driver\\geckodriver.exe")
    browser.get("http://204.209.76.218:8000/")
    created = browser.find_element_by_id("created")
    contact = browser.find_element_by_id("contact")
    about = browser.find_element_by_id("about")
    education = browser.find_element_by_id("education")
    skills = browser.find_element_by_id("skills")
    work = browser.find_element_by_id("work")
    name = browser.find_element_by_id("name")
    assert self.driver.find_element_by_id("created") != None
    assert self.driver.find_element_by_id("contact") != None
    assert self.driver.find_element_by_id("about") != None
    assert self.driver.find_element_by_id("education") != None
    assert self.driver.find_element_by_id("skills") != None
    assert self.driver.find_element_by_id("work") != None
    assert self.driver.find_element_by_id("name") != None
