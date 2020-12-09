# from typing import List

from selenium import webdriver

# from selenium.webdriver import ActionChains

driver = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
driver.get("http://leafground.com/pages/table.html")

# case 1
rowCountValue = driver.find_elements_by_xpath("//tr//td[1]")
NRC = len(rowCountValue)
print("No. of rows:", NRC)

# case 2
RowCount = driver.find_elements_by_xpath("//tr")
TRC = len(RowCount)

VRC = TRC - NRC + 1
# print(VRC)

VRC = str(VRC)

columnCount = driver.find_elements_by_xpath("//tr[" + VRC + "]//td")
print("No. of columns:", len(columnCount))

# case 3
print(driver.find_element_by_xpath("//tr//td[text()='Learn to interact with Elements']//following-sibling::td[1]").text)

# case 4
vc1 = driver.find_elements_by_xpath("//tr//td[2]")
vc = []
for vc2 in vc1:
    vc.append(vc2.text)

# Method 1
# vc.sort(key=lambda a: int(a[:-1]))
# print(vc)

# Method 2
temp = []
for key in vc:
    temp.append((key[:-1]))
temp = sorted(temp, key=int)
output = []
for key in temp:
    output.append(key + '%')
print("The lease value is", output)

minimumvalue = output[0]
print(minimumvalue)

valuexpath = "//tr//td[contains(text(),'" + minimumvalue + "')]//following-sibling::td[1]//input"

driver.find_element_by_xpath(valuexpath).click()
