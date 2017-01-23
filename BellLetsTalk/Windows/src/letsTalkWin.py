#! python3
# Bell Let's Talk Script
# Quinton Pryce
# 

import webbrowser, sys, requests, time
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

f = open('loginInfo.txt', 'r')
f2 = f.read().splitlines()
uid = f2[0]
email = f2[1]
password = f2[2]
inputNum = f2[3]
tweetsMade = 0 + int(inputNum)
f.close()

def waitForLogin():
  editPresent = len(browser.find_elements_by_id('global-new-tweet-button')) > 0
  while True:
    editPresent = len(browser.find_elements_by_id('global-new-tweet-button')) > 0
    if editPresent:
      break
def waitForID( string ):
  editPresent = len(browser.find_elements_by_id(string)) > 0
  while True:
    editPresent = len(browser.find_elements_by_id(string)) > 0
    if editPresent:
      break


def setUp():
  
  global browser
  browser = webdriver.Chrome('chromedriver.exe')
  browser.get('https://twitter.com/')
  browser.find_element_by_link_text('Log in').click()
  """
  #auto login for testing
  browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input').send_keys(uid)
  browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input').send_keys(password)
  browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]').click()
  """
  waitForLogin()
  
  for x in range(tweetsMade, 1001):
    f = open('loginInfo.txt', 'r')
    f2 = f.readlines()
    f.close()
    f = open('loginInfo.txt', 'w')
    f2[3] = str(x)
    f.writelines(f2)
    f.close()
    sleep(5)
    string = 'This is tweet #'
    string += str(x)
    string +=' for #BellLetsTalk '
    browser.find_element_by_id('global-new-tweet-button').click()
    
    browser.find_element_by_id('tweet-box-global').send_keys(string)
    browser.find_element_by_xpath('//*[@id="global-tweet-dialog-dialog"]/div[2]/div[4]/form/div[2]/div[2]/button').click()

setUp()