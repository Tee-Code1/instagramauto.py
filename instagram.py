from selenium import webdriver
import time
from selenium import webdriver



web = webdriver.Chrome()
web.get('https://www.instagram.com/accounts/login/')
url= ('https://www.instagram.com/explore/search/keyword/?q=')
time.sleep(2)

user_name = str(input('Enter Username or Email: '))
user = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user_name)
time.sleep(2)
password = str(input('Enter Password: '))

pas = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)

sign_in = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

time.sleep(5)

not_now = web.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

time.sleep(5)

not_now2 = web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()

time.sleep(2)
web.find_element_by_xpath("//a[@href=\"/explore/\"]").click()

explore = str(input('Enter Keywords: '))
exp = web.get(url + explore)
    
time.sleep(2)



# 
# web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input').click()

# time.sleep(2)
# explore= web.find_element_by_xpath('//*[@id="mount_0_0_IB"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div/div/svg').click()