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
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://gemini.google.com/app")
 # Get the browser window size

try:
    # Create an ActionChains instance
    actions = ActionChains(driver)

    # Move to the random coordinates and click
    actions.move_by_offset(928, 427).click().perform()
    time.sleep(2)
    print(f"Clicked at random coordinates ({"928"}, {"427"})")
    
    # Wait for the search input field to be clickable
    text_area = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "rich-textarea > div > p"))
        )

    # Input the search query
    text_area.send_keys("find me a song that goes something like this -  Im lookin for Mr Bubble Gum, I'm Mr ChickO Stick , try find something similar , give just the name of the song")

    # Find and click the send button
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class*='send-button-container'] > button"))
        )
    send_button.click()

    # Wait for the response to appear
    response_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "message-content[class*='model-response-text']"))
        )

        # Extract the response text
    time.sleep(5)
    response_text = response_element.text
    
    

except Exception as e:
    print(f"An error occurred: {e}")


finally:
    # Close the browser
    
    driver.quit()
print("Gemini Response:", response_text)

