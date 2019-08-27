from selenium import webdriver
import unittest

class SearchTests(unittest.TestCase):
    
    def setup(self):
        self.driver = webdriver.Chrome(r"C:\Users\koga\Documents\chromedriver_win32\chromedriver.exe")
        #self.driver.implicitly_wait(30)
        self.driver.get("https://google.com/")

    def test_search_image(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("phones")
        self.search_field.submit()
        #//で前のパスを省略，HTMLタグ[@要素名='要素']
        #find_elementsでリスト，1つしかないことが分かっているならelementでいい
        tab_name = self.driver.find_elements_by_xpath("//div[@class='hdtb-mitem hdtb-imb']")
        for t in tab_name:
            if t.text == "画像":
                image = t
        image.click()

    def tear_down(self):
        self.driver.close()

if __name__ == "__main__":
    test = SearchTests()
    test.setup()
    test.test_search_by_category()
    test.tear_down()