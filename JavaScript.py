from selenium import webdriver

# from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
driver.get("https://www.amazon.in/")

# Case 1:
# Method 1:
# print(driver.title)

# Method 2:
print(driver.execute_script("return document.title;"))

ClickOption = driver.find_element_by_link_text("Gift Cards")

# Case 2:
# Method 1:
# ClickOption.click()

# Method 2:
driver.execute_script("arguments[0].click();", ClickOption)

# Case 3:
# Method 1:
# print(driver.find_element_by_xpath("//*").text)

# Method 2:
print(driver.execute_script("return document.documentElement.innerText;"))

# Case 4:
# Method 1:
# driver.refresh()

# Method 2: (this below code is for confirmation of refreshed process)
try:
    driver.execute_script("history.go[0];")
    print("Page refreshed")
except Exception as e:
    print("Not refreshed", format(e))

# Case 5:
driver.execute_script("alert('Hi...');")
driver.switch_to.alert.accept()

# Case 6:
# Method 1:
inputText = driver.find_element_by_id("twotabsearchtextbox")
# inputText.send_keys("Mobile")

# Method 2:
driver.execute_script("document.getElementById('twotabsearchtextbox').value='mobile';")

# Case 7:
driver.execute_script("arguments[0].style.border='3px solid red';", inputText)

# Case 8:
# Method 1:
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Method 2:
position1 = driver.find_element_by_xpath("//*[text()='Best Sellers in Home & Kitchen']")
driver.execute_script("arguments[0].scrollIntoView(true);", position1)

# Method 3:
mouseaction = ActionChains(driver)
mouseaction.move_to_element(position1).perform()

# Method 4:
# position1.location_once_scrolled_into_view

# Case 9:
print(driver.execute_script("return navigator.userAgent;"))
