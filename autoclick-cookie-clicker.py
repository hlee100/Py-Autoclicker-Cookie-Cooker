from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

def selectLang():
    try:
        select_language = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "langSelect-EN"))
        )
        ActionChains(driver).click(select_language).perform()
    except Exception as e:
        print(f"Language selection failed: {e}")

def cookieAutoClick():
    selectLang()
    time.sleep(1)

    while True:
        try:
            clicky = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "bigCookie"))
            )
            ActionChains(driver).click(clicky).perform()
            time.sleep(0.1)
        except Exception as e:
            print(f"Error clicking cookie: {e}")

print("Program is running.")
cookieAutoClick()
    
    
