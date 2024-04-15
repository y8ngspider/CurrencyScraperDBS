from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re, os, yagmail, time
from datetime import datetime

def get_driver():
    #Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage') #For linux
    options.add_argument('no-sandbox') # Disable sandbox of browsers to have greater privileges
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--headless')
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options)
    driver.get('https://www.dbs.com.sg/personal/rates-online/foreign-currency-foreign-exchange.page')
    return driver


def get_exchange_rate():
    number = re.compile('\d\.\d\d\d')
    browser = get_driver()
    elements = WebDriverWait(browser, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[data-testid='exchangeRateToTestId']")))
    for element in elements:
        if (element.text).isalnum:
            exchange_rate_string = element.text
    exchangerate = float(number.search(exchange_rate_string)[0])
    print('Currency Data Fetched.')
    return exchangerate
    

def email(exchangerate,email_address):
    my_email= os.getenv('email') #Enter Sender Email
    my_password = os.getenv('password') #Enter Sender Password
    
    sender = my_email
    receiver = email_address

    current_time_stamp = datetime.strftime(datetime.now(),'%Y/%m/%d %H:%M:%S')

    subject = f'USD/SGD {current_time_stamp}'
    if 1/exchangerate > 1.33:
        contents = f'Exchange rate is currently {str(1/exchangerate)[0:7]} which is above 1.33 USD/SGD.'

    
    yag = yagmail.SMTP(user=sender, password=my_password)
    yag.send(to=receiver,subject=subject, contents=contents)
    print(f'Email Sent at {current_time_stamp}')

def main(email_address):
    while True:
        email(exchangerate=get_exchange_rate(),email_address=email_address)
        time.sleep(60)

main('example@gmail.com') #Enter Receiver Email Address
