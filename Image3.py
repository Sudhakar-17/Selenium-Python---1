from selenium import webdriver
import requests

options1 = webdriver.ChromeOptions()
options1.add_argument("start-maximized")
options1.add_argument("disable-infobars")
driver = webdriver.Chrome(options=options1, executable_path="E:\Software\Drivers\ChromeDriver\chromedriver.exe")
# driver.get("http://leafground.com/pages/Link.html")
driver.get("http://leafground.com/pages/Image.html")
links = driver.find_elements_by_css_selector("img")
for link in links:
    r = requests.get(link.get_attribute('src'))
    # print(link.get_attribute('href'), r.status_code)
    if r.status_code < 400:
        print(link.get_attribute('src'))
    else:
        print(link.get_attribute('src') + " is not available")
