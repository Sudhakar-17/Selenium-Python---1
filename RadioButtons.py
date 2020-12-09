from selenium import webdriver

driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://leafground.com/pages/radio.html")

#case 1
driver.find_element_by_xpath("//input[@id='yes']").click()

#case 2
xpath1 = "//label[contains(text(),'Find default selected radio button')]//following-sibling::label//input"

radio1 = driver.find_elements_by_xpath(xpath1)
print(len(radio1))

for radio2 in radio1:
    if radio2.is_selected():
        print("Yes", radio2.get_attribute("value"))
