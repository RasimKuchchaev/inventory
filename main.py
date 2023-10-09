import pickle

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import conf
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import lxml


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

s = Service(executable_path=r'C:\Users\Rasim\PycharmProjects\warface_inventory\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
  '''
})



try:
    driver.maximize_window()
    driver.get('https://market.vkplay.ru/inventory/1')
    time.sleep(10)

    driver.find_element(By.XPATH, conf.auth).click()
    time.sleep(20)

    email = ActionChains(driver)
    email = email.send_keys(conf.email).perform()
    time.sleep(5)

    press_enter = ActionChains(driver)
    press_enter = press_enter.send_keys(Keys.ENTER).perform()
    time.sleep(10)

    driver.switch_to.window(driver.window_handles[1])

    press_pasw = ActionChains(driver)
    press_pasw = press_pasw.send_keys(conf.pasw).perform()
    time.sleep(10)

    press_enter = ActionChains(driver)
    press_enter = press_enter.send_keys(Keys.ENTER).perform()
    time.sleep(10)



    # # html_source = driver.page_source
    # #
    # # bs4 = BeautifulSoup(html_source, 'lxml')
    # # items_count = bs4.find(class_=conf.item_count_inventory).text.split(" ")[-1]
    #
    # driver.find_element(By.CLASS_NAME, conf.button_my_pin_code).click()
    # print("conf.button_my_pin_code")


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
