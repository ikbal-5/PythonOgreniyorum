from githubUserİnfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element("xpath","//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element("xpath","//*[@id='password']").send_keys(self.password)

        time.sleep(1)
        self.browser.find_element("xpath","//*[@id='login']/div[4]/form/div/input[13]").click()
    def getFollowers(self):
        self.browser.get(f"https://github.com/ikbal-5?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements(BY.CSS_SELECTOR,".d-table.table-fixed")
        for i in items:
           self.followers.append(i.find_element(BY.CSS_SELECTOR,"link-gray.pl-1")).text

github = Github(username,password)

github.signIn()
github.getFollowers()
print(github.getFollowers)