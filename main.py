from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC

import logging, time

AMAZON_PRODUCT_LINK = "https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945/ref=sr_1_2?crid=1ZDXB7YRF1RXT&keywords=playstation+5&qid=1648454510&rnid=5367991051&s=videogames&sprefix=playstatio%2Caps%2C303&sr=1-2"
#TEST_LINK = "https://www.amazon.com.au/YPCC-Outdoor-Portable-Arrangement-Concerts/dp/B099F65H74/ref=sr_1_55?crid=2WC3Q6WH0O7H9&keywords=folding+picnic+table&qid=1648713405&sprefix=folding+picnic+table%2Caps%2C261&sr=8-55"

# AMAZON XPATHs
UNAVAILABLE_XPATH = "/html/body/div[2]/div[2]/div[6]/div[4]/div[4]/div[19]/div[1]/span"
AVAILABLE_XPATH = "/html/body/div[2]/div[2]/div[6]/div[4]/div[1]/div[2]/div/div/div/div/div/div/form/div/div/div/div/div[3]/div/div[4]/div/div[1]/span"

# FORM INFO
BUY_BUTTON_XPATH = '//*[@id="buy-now-button"]'
EMAIL_INPUT_XPATH = '//*[@id="ap_email"]'
CONTINUE_BUTTON_XPATH = '//*[@id="continue"]'
PASSWORD_INPUT_XPATH = '//*[@id="ap_password"]'
SUBMIT_BUTTON_XPATH = '//*[@id="signInSubmit"]'

# BILLING INFO
CONTINUE_XPATH = '/html/body/div[5]/div[2]/div[1]/form/div/div[1]/div[2]/span/a'
CREDIT_CONTINUE_XPATH = '/html/body/div[5]/div/div[2]/div[3]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/input'
BILLING_ADDRESS_XPATH = '/html/body/div[5]/div[1]/div[2]/div[1]/form/div/div[1]/div[2]/span/a'
IGNORE_PRIME_XPATH = '//*[@id="prime-declineCTA"]'
ORDER_XPATH = '/html/body/div[5]/div[1]/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input'

# ACCOUNT INFO
ACCOUNT_EMAIL = 'email@email.com'
ACCOUNT_PASSWORD = 'password123'

driver = webdriver.Firefox()
wait = ui.WebDriverWait(driver,5)

available = False
#interval = 0

start_time = time.ctime(time.time())

def c_print(message):
    print(time.ctime(time.time()) + " | " + message)

def order_function():
    try:
        buy_button = wait.until(EC.element_to_be_clickable((By.XPATH, BUY_BUTTON_XPATH)))
        buy_button.click()

        email_input = wait.until(EC.presence_of_element_located((By.XPATH, EMAIL_INPUT_XPATH)))
        email_input.send_keys(ACCOUNT_EMAIL)

        continue_button = wait.until(EC.presence_of_element_located((By.XPATH, CONTINUE_BUTTON_XPATH)))
        continue_button.click()

        password_input = wait.until(EC.presence_of_element_located((By.XPATH, PASSWORD_INPUT_XPATH)))
        password_input.send_keys(ACCOUNT_PASSWORD)

        continue_button = wait.until(EC.presence_of_element_located((By.XPATH, SUBMIT_BUTTON_XPATH)))
        continue_button.click()

        try:
            continue_button = wait.until(EC.presence_of_element_located((By.XPATH, CONTINUE_XPATH)))
            continue_button.click()

            continue_credit_button = wait.until(EC.presence_of_element_located((By.XPATH, CREDIT_CONTINUE_XPATH)))
            continue_credit_button.click()

            try:
                prime = wait.until(EC.presence_of_element_located((By.XPATH, IGNORE_PRIME_XPATH)))
                prime.click()

                order = wait.until(EC.presence_of_element_located((By.XPATH, ORDER_XPATH)))
                order.click()

                end_time = time.ctime(time.time())

                print("Began: " + start_time + "\n" + "Finished: " + end_time)

                driver.quit()
            except:
                order = wait.until(EC.presence_of_element_located((By.XPATH, ORDER_XPATH)))
                order.click()

                end_time = time.ctime(time.time())

                print("Began: " + start_time + "\n" + "Finished: " + end_time)

                driver.quit()
        except:
            c_print("You need to have your address information saved. Exiting.")
    except:
        c_print("Something went wrong! Trying again.")
        return order_function()

try:
    #driver.get(AMAZON_PRODUCT_LINK)
    driver.get(AMAZON_PRODUCT_LINK)

    while available != True:
        #if interval == 5:
        #    driver.get(TEST_LINK)
        try:
            available = driver.find_element(by=By.XPATH, value=BUY_BUTTON_XPATH).is_displayed()
        except:
            c_print("Product not available! Checking again.")
            driver.refresh()
        #    interval += 1 

    c_print("Product available! Checking out.")
    order_function()

except Exception as Argument:
    logging.exception("Something went wrong.")