import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def random_logpassw(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_names ():
    return random.choice(list(open("data\listnames.txt", "r")))

def random_surnames ():
    return random.choice(list(open("data\listsurnames.txt", "r")))

def random_about ():
    return random.choice(list(open("data\listabout.txt", "r")))