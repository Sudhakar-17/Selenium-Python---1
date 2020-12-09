from selenium import webdriver

driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://leafground.com/pages/Image.html")

# case 1
driver.find_element_by_xpath("//img[@src='../images/home.png']").click()
driver.back()
# case 2
