from data import *

i = 0
n = 3 #Number of registrations
driver = webdriver.Chrome('data\chromedriver.exe')
logpass = open("log_pass.txt", "a")
print('Загружено имен:', len(open("data\listnames.txt", "r").readlines()))
print('Загружено фамилий:', len(open("data\listsurnames.txt", "r").readlines()))
print('-------------------------\n')
while i < n:
    driver.get("http://84.201.143.169/register")
    password = random_logpassw(7, string.ascii_uppercase)
    login = random_logpassw(6, string.ascii_lowercase)
    driver.find_element_by_id("name").send_keys(random_names())
    driver.find_element_by_id("surname").send_keys(random_surnames())
    driver.find_element_by_id("email").send_keys(random_logpassw(10, string.ascii_uppercase)+'@gmail.com')
    driver.find_element_by_id("date").send_keys("20.12.2077")
    driver.find_element_by_id("about_me").send_keys("НЕ БЕЙТЕ ПАЛКОЙ")
    driver.find_element_by_id("username").send_keys(login)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("retype_password").send_keys(password)
    driver.find_element_by_id("submit").send_keys(Keys.ENTER)
    driver.get("http://84.201.143.169/logout")
    print('USERNAME: ' + login, file=logpass)
    print('PASSWORD: ' + password, file=logpass)
    print(' ', file=logpass)
    i = i + 1
    print("Кол-во регистраций: ", i)

driver.close()