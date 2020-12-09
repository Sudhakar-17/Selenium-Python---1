from selenium import webdriver

driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://leafground.com/pages/Button.html")

# case 1
driver.find_element_by_id("home").click()
print(driver.current_url, end='\n\n')
driver.back()

# case 2
positionCheck = driver.find_element_by_id("position")
print(positionCheck.text)
print(positionCheck.location)
print(positionCheck.size, end='\n\n')

# case 3
print(driver.find_element_by_id("color").get_attribute("style"), end='\n\n')

# case 4
sizeCheck = driver.find_element_by_id("size")
print("The size is {0}", format(sizeCheck.size))
