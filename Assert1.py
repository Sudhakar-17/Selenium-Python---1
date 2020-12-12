
from selenium import webdriver

driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://www.google.com/")
websiteTitle = driver.title

try:
    # assert "Google" in websiteTitle
    assert "Bing" in websiteTitle
    print("Title is Google")
except Exception as e:
    print("Title is not Google", format(e))

if "Googles" == websiteTitle:
    print("Title is Google")
else:
    print("Title is not Google")

driver.close()
