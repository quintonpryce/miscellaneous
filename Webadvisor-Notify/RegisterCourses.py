#! python3
# Script by Quinton Pryce

import webbrowser, sys, requests, time
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import subprocess
import os
f = open('workfile.log', 'r')
f2 = f.read().splitlines()
yourFName = f2[0]
yourLName = f2[1]
yourUID = f2[2]
yourPassword = f2[3]
f.close()

def setUp():
  global browser
  browser = webdriver.Chrome('/Users/quintonpryce/Desktop/Webadvisor-Notify/chromedriver')
  
  #########Open Links Page############
  browser.get('https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?TOKENIDX=4617017568&CONSTITUENCY=WBST&TYPE=M&PID=CORE-WBST')
  browser.find_element_by_link_text('Log In').click()
  browser.find_element_by_id('USER_NAME').send_keys(yourUID)
  browser.find_element_by_id('CURR_PWD').send_keys(yourPassword)
  browser.find_element_by_xpath('//*[@id="content"]/div[3]/form/div[2]/input').click()

  browser.find_element_by_link_text('Register and Drop Sections').click()

  if browser.find_element_by_id('LIST_VAR2_3') != "0 / 240":
    os.system("say Quinton, your course is open.")
  elif browser.find_element_by_id('LIST_VAR2_3') == "0 / 240":
    browser.close()
    setUp()
setUp()



#Fixed issue with multiple tickets - ELMS Order reference misplaced - Services ticket settings changed
