import string
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('data\chromedriver.exe') #driver location

def random_logpassw(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_list (list_location = " "):
    return random.choice(list(open(list_location, "r")))

def connection_error ():
    print('Не удается подключиться')
    time.sleep(5)
    driver.close()
    exit()