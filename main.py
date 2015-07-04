from linkedin import linkedin
import json
import time
import webbrowser
import os
import subprocess
import signal
import psutil

CONSUMER_KEY = '77mdob21napbd1'
CONSUMER_SECRET = '4yPxqdCb3hLodTUV'
USER_TOKEN = "1a817617-f118-4c12-8025-84e0d89132a8"
USER_SECRET = "c331a7f6-7af5-4da5-a886-d182bfbcca75"

RETURN_URL = 'http://localhost:8000'

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                          USER_TOKEN, USER_SECRET, 
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())

application = linkedin.LinkedInApplication(authentication)


connections = application.get_connections(selectors=['siteStandardProfileRequest', 'first-name', 'last-name'], params={'start':600, 'count':100})
# companies = application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}], params={'keywords': 'apple microsoft'})

def chromeTab( url ):
	pid = webbrowser.open_new_tab(url)
   	return pid

for x in connections['values']:
	print x['lastName']
	print x['firstName']
	if ('siteStandardProfileRequest' in x):
		url = x['siteStandardProfileRequest']['url']
		print chromeTab(url)
		time.sleep(0.5)

#pid = os.spawnlp(os.P_NOWAIT, "./firefox.sh", "http://godsadsaogle.com")

# pro = subprocess.Popen(['./firefox.sh', 'http://mailjet.com'])
# print pro.pid
# time.sleep(6)
# p = psutil.Process(pro.pid + 1)
# print "killing", pro.pid + 1, p
# p.kill()  #or p.kill()

# from webbrowser import open_new_tab
# open_new_tab("http://google.com")

