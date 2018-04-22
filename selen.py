# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # modul
import time


name = "Zenobiusz"
last_name = "Krakowski"
telephone = "123123123"
valid_email = "zenobiusz.krakowski@o2.pl"
valid_password = "ZrdGxzOe"
birth_date = "29021985"
Country = "Polska"
City = "Warszawa"
Postal_Code = "00-113"
Street = "Emilii Plater 53"
Position = "Technical Manager"
Company = "Croma Sp. z o.o."
Start_date = "05042001"


class CV_Kreator(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
    #    self.driver = webdriver.Firefox(executable_path="D:\Justyna\geckodriver")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_szablon(self):
        driver = self.driver
        driver.get('https://www.cv.pl/')
        self.driver.implicitly_wait(15)
        time.sleep(2)

        link = driver.find_element_by_xpath('//*[@id="top"]/div[@class="content-wrapper"]/ul[@id="menu"]/li[1]/a')
        link.click()
        driver.implicitly_wait(15)
        time.sleep(3)

        szablon = driver.find_element_by_xpath(' //*[@class="single-template m-r38"][3]/a[1]/img')
        szablon.click()
        driver.implicitly_wait(15)
        time.sleep(3)

        mail = driver.find_element_by_xpath('//input[@name="username"]')
        mail.send_keys('zenobiusz.krakowski@o2.pl')
        save = driver.find_element_by_id('save-email')
        save.click()
        driver.implicitly_wait(15)
        time.sleep(3)

        mail_2 = driver.find_element_by_xpath('//form[@id="user-login-form"]//*[@name="username"]')
        mail_2.send_keys(valid_email)
        password = driver.find_element_by_xpath('//*[@class="last"]/input[@class="full CIF-Required"]')
        password.send_keys(valid_password)
        submit = driver.find_element_by_xpath('//*[@class="submit"]')
        submit.click()
        driver.implicitly_wait(15)

     #   edycja = driver.find_element_by_xpath('//*[@class="edit-menu"]//*[@title="Edytuj dane"]')
      #  edycja.click()
       # name = driver.find_element_by_xpath("//form[@id='general-form']//*[@class='controls']")
        #name.click()
    #    name.clear()
     #   name.send_keys(name)
      #  last_name = driver.find_element_by_xpath("//form[@id='general-form']//*[@class='controls']/input[@class='i100 CIF-Required xh-highlight']")
       # last_name.send_keys(last_name)
        #driver.implicitly_wait(15)

    #    experience = driver.find_element_by_xpath("//*[@id='candidate-menu-0']//*[text()='Doświadczenie zawodowe']")
 #       experience.click()
  #      add_experience - driver.find_element_by_xpath('//*[@id="c-menu-0"]//*[@class="btn exp-add-btn"]')
   #     add_experience.click()
    #    checkbox = driver.find_element_by_xpath('/*[@name="exp_still_working"]')
     #   checkbox.click()

  #      gender_switch = driver.find_element_by_xpath('//*[@name="gender"]//option[@value="2"]')
   #     gender_switch.location_once_scrolled_into_view


#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)

#    try:
#        page_loaded = wait.until_not(
#            lambda driver: driver.current_url == login_page
        #    lambda driver: driver.find_element_by_xpath
#        )
#    except TimeoutException:
#        self.fail("Loading timeout expired")

#    self.assertEqual(
#        driver.current_url,
#        correct_page,
#        msg="Successful Login"


 #   def tearDown(self):
 #       self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
