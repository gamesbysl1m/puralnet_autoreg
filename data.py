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

def random_date():
    return (str(random.randint(1, 29))+'.'+str(random.randint(1, 12))+'.'+str(random.randint(1980, 2007)))

def user_activity():
    a = 1
    followers_count = 0
    followers_count_max = 25
    url = driver.current_url
    users_count = url.replace("http://84.201.143.169/user/id", "")
    counter = random.randint(10, int(users_count)-80)
    print('Number of follows needed: ', counter)
    print('Max follows: ', followers_count_max)
    while a < counter and followers_count < followers_count_max:
        driver.get("http://84.201.143.169/user/id" + str(random.randint(0, int(users_count))))
        try:
            driver.find_element_by_class_name('btn-success').send_keys(Keys.ENTER)
            followers_count = followers_count + 1
            a = a + 1
            print(followers_count)
            time.sleep(1)
        except Exception:
            followers_count = followers_count + 1
            a = a + 1
            print('Subscription error ', followers_count)
            pass


def connection_error ():
    print('Unable to connect, shutdown')
    time.sleep(5)
    driver.close()
    exit()