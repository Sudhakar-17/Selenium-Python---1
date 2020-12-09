from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import win32clipboard

driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://leafground.com/pages/Edit.html")

# Case 1
driver.find_element_by_id("email").send_keys("sudhakar.personal@gmail.com")

# Case 2
driver.find_element_by_xpath("//input[@value='Append ']").send_keys("text appended")
copy2 = driver.find_element_by_xpath("//input[@value='Append ']").send_keys(Keys.TAB)

# Case 3

# Method 1
copy1 = driver.find_element_by_xpath("//input[@name='username' and @value='TestLeaf']")
copy1.send_keys(Keys.CONTROL, 'a')
copy1.send_keys(Keys.CONTROL, 'c')
win32clipboard.OpenClipboard()
text = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print(text)

# Method 2:
print(driver.find_element_by_xpath("//input[@name='username' and @value='TestLeaf']").get_property('value'))

# Method 3:
print(driver.find_element_by_xpath("//input[@name='username' and @value='TestLeaf']").get_attribute('value'))

# Method 4:
chek = driver.find_element_by_xpath("//input[@name='username' and @value='TestLeaf']").text
print(chek)

# Method 5:
text1 = driver.find_element_by_xpath("//input[@name='username' and @value='TestLeaf']")
text2 = driver.execute_script("arguments[0].text;", text1)
print(text2)

# Case 4

driver.find_element_by_xpath("//input[@name='username' and @value='Clear me!!']").clear()

# Case 5

disableCheck = driver.find_element_by_xpath("//input[@type='text' and @disabled='true']").is_enabled()
print("Is the field is enable: ", disableCheck)

if disableCheck is True:
    print("The mentioned field is Enable")
else:
    print("The mentioned field is disable")

# driver.execute_script("document.documentElement.innerText")
