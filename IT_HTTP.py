"""*************************************************************************************************
	#function set to login and read web content to Json and print
	HTTP_login(username,password,login_url)
	HTTP_getJson(url)
	printdict(mydict,k)








Last Modified by:
wind.wang@syniverse.com 20181126
*************************************************************************************************"""


"""*************************************************************************************************
#function set to login and read web content to Json and print
HTTP_login user username and password to log in a URL and return opener for HTTP_getJson to use

HTTP_getJson open an URL and get the content in Json format

printdict print the Json output

How to get login URL ?
Open Firefox, click F12,input url, input username,password, hit login
In debug window, click network, check the content of the first POST to get login URL.

How to get URL for HTTP_getJson ?
After login,navigate to the target web page, select all the option on webpage
click "submit"/"search" or other button to send the request
in F12 window of Firefox, locate the url in the POST message


hank.chen@syniverse.com 20181126 summariesed by Wind
*************************************************************************************************"""
import urllib.request
from http import cookiejar
from http import cookies
from urllib import parse
import ssl
import json
import getpass


def HTTP_login(username,password,login_url):
	global opener

	data = {"j_username": username.strip(),
	        "j_password": password.strip()
	        }
	
	cookie=cookiejar.CookieJar()
	
	cookie_handle=urllib.request.HTTPCookieProcessor(cookie)
	opener=urllib.request.build_opener(cookie_handle)
	
	data=urllib.parse.urlencode(data).encode('utf-8')
	request=urllib.request.Request(login_url,data=data)
	response=opener.open(request)



def HTTP_getJson(url):
	global opener
	request=urllib.request.Request(url)
	response=opener.open(request)
	html = response.read().decode('utf-8')
	dict_json = json.loads(html)
	return dict_json



def printdict(mydict,k):

	for item in mydict:
		if isinstance(mydict[item], list):
			print ("%s%s:" %(k,item))
			k += "    "
			for i in mydict[item]:
				print ("%s===============" %k)
				if isinstance(i, dict):
					printdict(i,k)
		else:
			print ("%s%s:%s" %(k,item, mydict[item]))

def DEMO():
	pwd="XXXXXX"
	HTTP_login("g707414",pwd,'https://reportr.syniverse.com/j_spring_security_check')
	gid="g707414"
	startMonth = "01-2018"
	endMonth = "01-2018"
	customerType = "External"
	url = "https://reportr.syniverse.com/piAnalysis/fetchSummary?queues=null&products=null&personGid=" + gid + "&startMonth=" + startMonth + "&endMonth=" + endMonth +  "&type=Organization&customerType=" + customerType +"&severity=any&submittedINCs=undefined"
	
	print ("%s:%s" %(gid,url))
	dict_json = HTTP_getJson(url)
	printdict(dict_json,"")
	print(dict_json)
	print(dict_json["totalPiCount"])
	print(dict_json["teamWise"])
	print(dict_json["teamWise"][0]["team"])


DEMO()

"""*************************************************************************************************
#Selenium function sets enable user to simulate human to process on webpage
HTTP_selenium_login use username and password to login a url

HTTP_getJson open an URL and get the content in Json format

printdict print the Json output

How to get login URL ?
Open Firefox, click F12,input url, input username,password, hit login
In debug window, click network, check the content of the first POST to get login URL.

How to get XPATH
After login,navigate to the target web page, select all the option on webpage
click "submit"/"search" or other button to send the request
in F12 window of Firefox, locate the url in the POST message


hank.chen@syniverse.com 20181126 summariesed by Wind
*************************************************************************************************"""

from selenium import webdriver
import time
import selenium
from selenium.webdriver.common.keys import Keys 

def HTTP_selenium_login(url,username,password):

	global driver
	#Login Report R
	try:
		driver.get(url)  
		#driver.maximize_window()
	#except selenium.common.exceptions.WebDriverException, ConnectionAbortedError:
	except Exception as e:
		print(e)
		driver = webdriver.Firefox()
		driver.maximize_window()
		#print(dir(driver))
		home_handle = driver.current_window_handle
		
		driver.get(url)
		
	elem_user = driver.find_element_by_xpath('//*[@id="username"]')  
	elem_user.send_keys(username) 
	
	elem_pwd = driver.find_element_by_xpath('//*[@id="password"]')
	elem_pwd.send_keys(password)  
 
	while True:
		try:
			elem_pwd.send_keys(Keys.RETURN)
		except:
			pass
		else:
			break 



def HTTP_selenium_click_xpath(x_path):
	while True:
		try:
			driver.find_element_by_xpath(x_path).click() 
		#The first 2 except is for illustration, can be delete 
		except selenium.common.exceptions.NoSuchElementException:
			print(x_path+" No Such Element Exception")
			pass#if element not found,pass and try again
		except selenium.common.exceptions.ElementNotInteractableException:
			print(x_path+"Element Not Interactable Exception")
			pass
		except Exception as e:
			print(x_path +" "+str(e))
			pass
		else:
			break
