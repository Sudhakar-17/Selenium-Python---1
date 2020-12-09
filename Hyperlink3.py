from selenium import webdriver

driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://leafground.com/pages/Link.html")
links = driver.find_elements_by_tag_name('a')
print(len(links))
for link in links:
    print(link.get_attribute('href'))
