# SONGMASTER
# 16.8.2025
# ITAY SCORIK
# ROEI KORIAT

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://chat.openai.com/")

    # Wait until the textarea is present
    search_bar = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )

    # Type the question
    question = "whats 1+1"
    search_bar.send_keys(question)

    # Wait for the send button and click it
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary')]"))
    )
    submit_button.click()

    # Wait for the response to appear
    response_div = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'result-streaming')]"))
    )

    # Get the response text
    response_text = response_div.text
    print(f"ChatGPT answer: {response_text}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
