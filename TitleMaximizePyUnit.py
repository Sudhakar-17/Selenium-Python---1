import unittest

# import HTMLTestRunner
from selenium import webdriver


class basicTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("E:\Software\Drivers\ChromeDriver\chromedriver.exe")
        self.browser.get("https://www.youtube.com/")

    def test_Title(self):
        name = self.browser.title
        print(name)

    def test_WindowSize(self):
        self.browser.set_window_size(300, 400)

    def tearDown(self):
        self.browser.close()
        self.browser.quit()


# def suite():
#     suiteTest = unittest.TestSuite()
#     suiteTest.addTest(basicTest("test_Title"))
#     suiteTest.addTest(basicTest("test_WindowSize"))
#     return suiteTest


if __name__ == '__main__':
    unittest.main()
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())

    # filepath = 'D:\MyPractice\Python_Program\PythonPytest1\pyresult.html'
    # fp = open(filepath, 'w')
    # runner = HTMLTestRunner.HTMLTestRunner(HTMLTestRunner)
    # runner.run(suite())
    # fp.close()
    # unittest.main()
