#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import random
timeout = 2

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/accounts/login/")
try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Loading Log in...")

driver.find_element_by_xpath(
    "//input[@name='username']").send_keys("username")
driver.find_element_by_xpath(
    "//input[@name='password']").send_keys("password")
driver.find_element_by_xpath("//button[contains(.,'Log In')]").click()
sleep(2)
try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Scrapped...")

driver.get(
    "https://www.instagram.com/direct/t/340282366841710300949128139139074234489/")


def lo():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea"))).send_keys("hi there")
    driver.find_element_by_xpath(
        "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()


sleep(3)
driver.find_element_by_xpath(
    "/html/body/div[4]/div/div/div/div[3]/button[2]").click()
sleep(2)


driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/button").click()


for n in range(1, 9):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input"))).send_keys("@pheona_em")
    sleep(1)

    driver.find_element_by_xpath(
        f"/html/body/div[4]/div/div/div[2]/div[2]/div[{n}]/div/div[3]/button/span").click()


driver.find_element_by_xpath(
    "/html/body/div[4]/div/div/div[1]/div/div[2]/div/button").click()

for i in range(1):
    lo()

# driver.find_element_by_xpath(
#     "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]/a/div").click()
# sleep(2)

# # /html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[2]/a/div


# driver.quit()

# # file handle fh

# def red(i):
#     text_file = open("mentions.txt", "r")
#     l = []
#     lines = text_file.readlines()
#     for line in lines:
#         l.append(line)
#     l = line.split(",")

#     # f = open("mentions.txt", "r")
#     # for x in f:

#     driver.find_element_by_xpath(
#         "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").click()
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
#         (By.XPATH, "//form[@class='X7cDz']//textarea[contains(@placeholder,'Add')]"))).send_keys(l[i])
#     driver.find_element_by_xpath(
#         "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button").send_keys(Keys.ENTER)


# for i in range(5):
#     red(i)
#     sleep(2)
#     driver.get("https://www.instagram.com/p/CFZy1IsHvgc/")

# driver.quit()
