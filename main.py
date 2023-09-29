from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import conf
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


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
    print("1")
    driver.find_element(By.XPATH, conf.auth).click()
    time.sleep(20)
    print("2")
    # driver.switch_to.alert()
    actions = ActionChains(driver)
    actions = actions.send_keys('asdasdasd')
    actions = actions.send_keys(Keys.TAB)
    actions = actions.send_keys('ggfdgdfgfd')
    actions = actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(10)
    print("3")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
