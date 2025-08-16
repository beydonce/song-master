# SONGMASTER
# 16.8.2025
# ITAY SCORIK
# ROEI KORIAT

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://chatgpt.com/")
 # Get the browser window size

try:
    # Create an ActionChains instance
    actions = ActionChains(driver)

    # Move to the random coordinates and click
    actions.move_by_offset(928, 427).click().perform()

    print(f"Clicked at random coordinates ({"928"}, {"427"})")
    time.sleep(2)
    search_bar = driver.find_element(By.ID, "prompt-textarea")
    
    search_bar.send_keys("whats 1+1")
    time.sleep(1)
    
    button = driver.find_element(By.ID, "composer-submit-button")
    button.click()
    

except Exception as e:
    print(f"An error occurred: {e}")


finally:
    # Close the browser
    
    driver.quit()


