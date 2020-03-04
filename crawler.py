from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
def tor_driver():
	opts = Options()
	opts.add_argument("--incognito")
	proxy = "socks5://localhost:9050"
	opts.add_argument('--proxy-server={}'.format(proxy))
	opts.add_argument('--headless')
	opts.add_argument('--disable-gpu')
	ua = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
	opts.add_argument("user-agent={}".format(ua))
	driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe',options=opts)
	driver.get('http://myip.briian.com/')
	print(driver.find_element_by_xpath("/html/body/p[2]").text)
	driver.close()

for i in range(5):
	os.system("start /b cmd /c .\\tor_browser\\Tor\\tor.exe")
	tor_driver()
	os.system("TASKKILL /F /IM tor.exe")
