import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def random_logpassw(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_names ():
    return random.sample(list(open("data\listnames.txt", "r")), 1)

def random_surnames ():
    return random.sample(list(open("data\listsurnames.txt", "r")), 1)