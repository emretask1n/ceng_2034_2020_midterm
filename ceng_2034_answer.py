import os
import requests
import threading


os.system("clear")

print(os.name)

print(os.getpid())

print(os.getloadavg())

load1 , load5 , load15 = os.getloadavg()

print("Load average of last 5 minute is: ", load5)

CPUs = os.cpu_count()

print("Cpu core count is: ", CPUs)

def url_check(url):
	r = requests.head(url)
	if r.status_code == 200:
		print(url ," is a valid url")
	else:
		print(url ,"is not valid")

#url_check("https://api.github.com")
#url_check("https://www.tpython.org")
#url_check("http://bilgisayar.mu.edu.tr")
#url_check("http://akrepnalan.com/ceng2034")
#url_check("https://github.com/caesarsalad/wow")

thread1=threading.Thread(target=url_check, args=("https://api.github.com",))
thread2=threading.Thread(target=url_check, args=("https://www.python.org",))
thread3=threading.Thread(target=url_check, args=("http://bilgisayar.mu.edu.tr",))
thread4=threading.Thread(target=url_check, args=("http://akrepnalan.com/ceng2034",))
thread5=threading.Thread(target=url_check, args=("https://github.com/caesarsalad/wow",))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()



