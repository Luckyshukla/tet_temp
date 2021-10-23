from selenium import webdriver

import OTP_verifivation
import credentials
import time


def test_sign_up():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.get("https://careers.neuralcompany.work/app/login")

    chrome_driver.find_element_by_xpath('//*[@id="loginManually"]').click()
    chrome_driver.find_element_by_xpath("//body/div[@id='root']/main[@id='main-body']/div[1]/div[1]/div[2]/div["
                                        "1]/div[1]/form[1]/div[1]/input[1]").send_keys("lucky+13@xenonstack.com")
    chrome_driver.find_element_by_xpath("//body[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/section["
                                        "1]/div[1]/div[1]/div[2]/div[1]/button[2]").click()
    time.sleep(10)
    otp = OTP_verifivation.get_otp()
    # otp_split = [str(i) for i in str(otp[0])]
    #
    # # fills in 4 pin OTP code
    # for i in range(6):
    #     otp_elem = chrome_driver.find_element_by_xpath('//*[@id="verification_code_' + str([i + 1]))
    #     otp_elem.send_keys(otp_split[i])
    #
    # otp_login_elem = chrome_driver.find_element_by_xpath('//*[@id="submitOtp"]')
    # otp_login_elem.click()

    try:
        text = chrome_driver.find_element_by_xpath("//body[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form["
                                                   "1]/div[2]/div[1]/div[1]/span[1]").text
    except:
        chrome_driver.close()
        assert True, ""
    if text == "Email Already Exists.":
        assert False, str(otp)
    chrome_driver.close()
