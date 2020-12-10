import unittest
from selenium import webdriver


class DatePickerTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
        self.driver.maximize_window()

    def test_date_pick(self):
        driver = self.driver
        driver.get("https://jqueryui.com/datepicker/")
        frame = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(frame)
        datePickerBox = driver.find_element_by_id("datepicker")
        datePickerBox.click()
        driver.find_element_by_xpath("//a[@class = 'ui-state-default'][text()='4']").click()
        print(datePickerBox.get_attribute('value'))
        self.assertEqual(datePickerBox.get_attribute('value'), "12/05/2020")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
