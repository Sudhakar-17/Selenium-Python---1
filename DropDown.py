from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://leafground.com/pages/Dropdown.html")

# case 1
dropDownCount = driver.find_elements_by_xpath("//select[@class='dropdown']//option")
print("Total no. of dropdown list is", len(dropDownCount)-1)

# case 2
selection1 = Select(driver.find_element_by_id("dropdown1"))
selection1.select_by_index(2)

# case 3
selection1 = Select(driver.find_element_by_name("dropdown2"))
selection1.select_by_value("1")

# case 4
selection1 = Select(driver.find_element_by_id("dropdown3"))
selection1.select_by_visible_text("Loadrunner")

# case 5
selection2 = driver.find_element_by_xpath("//option[contains(text(),'You can also use sendKeys to select')]//parent::select")
selection2.send_keys("Appium")

# case 6

selection1 = Select(driver.find_element_by_xpath("//select[@multiple]"))

selection1.select_by_index(1)
selection1.select_by_index(2)
selection1.select_by_index(3)

