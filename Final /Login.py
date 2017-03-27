from selenium import webdriver 	
import time 

def FB_login():
	browser=webdriver.Firefox()
	browser.get('https://www.facebook.com')
	print("Loggin in Facebook")
	time.sleep(2)
	user=browser.find_elements_by_css_selector('#email')
	user[0].send_keys('pradhvanbisht@gmail.com')
	password=browser.find_elements_by_css_selector('#pass')
	with open('test.txt', 'r') as myfile:   #Don't be an idiot and store the password in the text file 
    	Password=myfile.read().replace('\n', '') #Reads password from a text file 
	password[0].send_keys(Password)
	login=browser.find_elements_by_css_selector('#u_0_q')
	login[0].click()
	print('Login Sucessfull')
	browser.close()

def Twitter_login():
	browser=webdriver.Firefox()
	browser.get('https://www.twitter.com')
	time.sleep(2)
	login=browser.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')
	login[0].click()
	print("Loggin in Twitter")
	user=browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')
	user[0].send_keys('pradhvanbisht@gmail.com')
	user=browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')
	with open('test.txt', 'r') as myfile:   #Reads password from a text file 
    	Password=myfile.read().replace('\n', '')
	user.send_keys(Password)
	LOG=browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
	LOG[0].click()
	print("Login Sucessfull")
	browser.close()

def Gmail_login():
	browser=webdriver.Firefox()
	browser.get('https://www.gmail.com')
	time.sleep(2)
	user=browser.find_elements_by_id('Email')
	user[0].send_keys('pradhvanbisht@gmail.com')
	login=browser.find_elements_by_id('next')
	login[0].click()
	print("Loggin in Gmail")
	time.sleep(5)
	user=browser.find_elements_by_xpath('//*[@id="Passwd"]')
	with open('test.txt', 'r') as myfile:   #Reads password from a text file 
    	Password=myfile.read().replace('\n', '')
	user[0].send_keys(Password)
	LOG=browser.find_elements_by_css_selector('#signIn')
	LOG[0].click()
	print("Login Sucessfull")
	browser.close()

print ("Welcome to custom login.\nPlease enter your choice : ")
Choice = raw_input("Gmail \t Facebook \t Twitter ").lower()

if Choice =='gmail':
	print ("Choice read as Gmail \n")
	Gmail_login()
elif Choice == 'twitter':
	Twitter_login()
elif Choice == 'facebook':
	FB_login()

