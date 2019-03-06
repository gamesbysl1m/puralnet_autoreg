from data import *

i = 0
n = 1 #Number of registrations
logpass = open("log_pass.txt", "a")
print('Загружено имен:', len(open("data\listnames.txt", "r").readlines()))
print('Загружено фамилий:', len(open("data\listsurnames.txt", "r").readlines()))
print('Загружено "О себе":', len(open("data\listabout.txt", "r").readlines()))
print('-------------------------\n')

while i < n:
    driver.get("http://84.201.143.169/register")
    if driver.title != 'PuralNet':
        connection_error()
    password = random_logpassw(7, string.ascii_uppercase + string.ascii_lowercase + string.digits)
    login = random_logpassw(6, string.ascii_lowercase)
    driver.find_element_by_id("name").send_keys(random_list("data\listnames.txt"))
    driver.find_element_by_id("surname").send_keys(random_list("data\listsurnames.txt"))
    driver.find_element_by_id("email").send_keys(random_logpassw(10, string.ascii_uppercase) + '@gmail.com')
    driver.find_element_by_id("date").send_keys("20.12.2077")
    driver.find_element_by_id("about_me").send_keys(random_list("data\listabout.txt"))
    driver.find_element_by_id("username").send_keys(login)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("retype_password").send_keys(password)
    driver.find_element_by_id("submit").send_keys(Keys.ENTER)
    driver.get("http://84.201.143.169/logout")
    if driver.title != 'PuralNet':
        connection_error()
    print('USERNAME: ' + login, file=logpass)
    print('PASSWORD: ' + password, file=logpass)
    print(' ', file=logpass)
    i = i + 1
    print("Кол-во регистраций: ", i)

logpass.close()
driver.close()