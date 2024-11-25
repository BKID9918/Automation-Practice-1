from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from Pages.base_page import Page


class JordanColorway(Page):
    jordan_name = (By.CSS_SELECTOR, "[href='https://www.nike.com/jordan']")
    new_releases = (By.CSS_SELECTOR, "[href='https://www.nike.com/w/jordan-37eef']")

    def open_main_page(self):
        self.driver.get('https://www.nike.com/')

    def find_jordan_elements(self):
        return self.driver.find_elements(*self.jordan_name)

    def hover_over_jordan_element(self):
        element = self.find_element(*self.jordan_name)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def wait_for_Jordan_be_clickable_click(self):
        self.wait.until(EC.element_to_be_clickable(self.jordan_name), f' Element by {self.jordan_name} is not clickable').click()

    def wait_for_Jordan_to_be_clickable(self):
       self.wait.until(EC.element_to_be_clickable(self.jordan_name), f' Element by {self.jordan_name} is not clickable')

    def click_new_releases(self):
        self.driver.find_element(*self.new_releases).click()

