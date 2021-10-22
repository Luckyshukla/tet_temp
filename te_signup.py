from selenium import webdriver
import credentials


def test_sign_up():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.get("https://careers.neuralcompany.work/app/login")
    user = credentials.test_credentials.username()
    chrome_driver.find_element_by_xpath("//button[@id='loginManually']").click()
    chrome_driver.find_element_by_xpath("//body/div[@id='root']/main[@id='main-body']/div[1]/div[1]/div[2]/div["
                                        "1]/div[1]/form[1]/div[1]/input[1]").send_keys(user)
    chrome_driver.find_element_by_xpath("//body[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/section["
                                        "1]/div[1]/div[1]/div[2]/div[1]/button[2]").click()
    try:
        text = chrome_driver.find_element_by_xpath("//body[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form["
                                                   "1]/div[2]/div[1]/div[1]/span[1]").text
    except:
        chrome_driver.close()
        assert True, ""
    if text == "Email Already Exists.":
        assert False, "Email Already Exists."
    chrome_driver.close()
