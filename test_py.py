import time
import pandas as pd
import pytest
import os
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.remote.webelement import WebElement

import credentials.test_credentials

def test_login_page():
    # i = 0
    # data = pd.read_csv('credentials.csv')
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://careers.neuralcompany.work/app/login')
    chrome_driver.maximize_window()
    #user = config('USER')
    user = credentials.test_credentials.username()
    password = credentials.test_credentials.password()
    each_iteration_sleep = credentials.test_credentials.sleep_time_each_iteration()
    final_wait_time = credentials.test_credentials.total_wait()
    chrome_driver.find_element_by_id("tpt_loginUsername").send_keys(user)
    chrome_driver.find_element_by_id("tpt_loginPassword").send_keys(password)
    # i += 1
    sleep(each_iteration_sleep)
    chrome_driver.find_element_by_id("loginButton").click()
    sleep(each_iteration_sleep)
    try:
        text = chrome_driver.find_element_by_xpath("//button[contains(text(),'Start Test')]").text
    except:
        chrome_driver.close()
        assert False, "Test Failed Drive not available"
    if text == "Start Test":
        assert True, "Test Passed"
        chrome_driver.find_element_by_xpath("//button[contains(text(),'Start Test')]").click()
        sleep(2)
        window_after = chrome_driver.window_handles[1]
        chrome_driver.switch_to.window(window_after)
        chrome_driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div["
                                            "1]/div[4]/label[1]/span[1]").click()
        sleep(each_iteration_sleep)

        chrome_driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div["
                                            "1]/div[5]/button[1]").click()
        sleep(each_iteration_sleep)

    for option in range(2):
        chrome_driver.find_element_by_class_name("option-1").click()
        sleep(each_iteration_sleep)
        chrome_driver.find_element_by_xpath("//button[contains(text(),'Submit & Next')]").click()
        sleep(each_iteration_sleep)
    # self.driver.find_element_by_xpath("//span[contains(text())]")
    # if self.driver.find_element_by_xpath("//button[contains(text(),'Finish Test')]").click():
    #     self.driver.quit()
    # WebElement
    element = chrome_driver.find_element_by_xpath('//*[@id="navigation-menu-right"]/li[2]/div/div/div/div')
    sleep(final_wait_time)
    chrome_driver.close()


test_login_page()
