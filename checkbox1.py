from selenium import webdriver

# from selenium.webdriver import ActionChains

driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://leafground.com/pages/checkbox.html")

# case 1
list1 = ["Java", "VB"]
for list2 in list1:
    driver.find_element_by_xpath("//label[contains(text(),'Select the languages that you know?')]//following-sibling::div//input//parent::div[text()='" + list2 + "']//input").click()


# case 2
check2 = driver.find_element_by_xpath(
    "//label[contains(text(),'Confirm Selenium is checked')]//following-sibling::div//input")
if check2.is_selected():
    print("Option is checked")

# case 3
check3 = driver.find_elements_by_xpath(
    "//label[contains(text(),'DeSelect only checked')]//following-sibling::div//input")

for check4 in check3:
    if check4.is_selected():
        check4.click()
    else:
        continue

# case 4
check5 = driver.find_elements_by_xpath(
    "//label[contains(text(),'Select all below checkboxes ')]//following-sibling::div//input")

for check6 in check5:
    check6.click()
