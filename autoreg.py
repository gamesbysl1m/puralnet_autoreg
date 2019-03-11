from data import *

current_registrations_count = 0
registrations_count = 3
logpass = open("log_pass.txt", "a")
print('Names loaded:', len(open("data\listnames.txt", "r").readlines()))
print('SurNames loaded:', len(open("data\listsurnames.txt", "r").readlines()))
print('Uploaded "about me":', len(open("data\listabout.txt", "r").readlines()))
print('-------------------------\n')

try:
    while current_registrations_count < registrations_count:
        driver.get("http://84.201.143.169/register")
        if driver.title != 'PuralNet':
            connection_error()
        password = random_logpassw(7, string.ascii_uppercase + string.ascii_lowercase + string.digits)
        login = random_logpassw(6, string.ascii_lowercase)
        driver.find_element_by_id("name").send_keys(random_list("data\listnames.txt"))
        driver.find_element_by_id("surname").send_keys(random_list("data\listsurnames.txt"))
        driver.find_element_by_id("email").send_keys(random_logpassw(10, string.ascii_uppercase) + '@gmail.com')
        driver.find_element_by_id("date").send_keys(random_date())
        driver.find_element_by_id("about_me").send_keys(random_list("data\listabout.txt"))
        driver.find_element_by_id("username").send_keys(login)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("retype_password").send_keys(password)
        driver.find_element_by_id("submit").send_keys(Keys.ENTER)
        current_registrations_count += 1
        print("Number of registrations: ", current_registrations_count)
        user_activity()
        driver.get("http://84.201.143.169/logout")
        if driver.title != 'PuralNet':
            connection_error()
        print('USERNAME: ' + login, file=logpass)
        print('PASSWORD: ' + password, file=logpass)
        print(' ', file=logpass)
        print('-------------------------')

except Exception:
    time.sleep(3)
    pass

logpass.close()
driver.close()
