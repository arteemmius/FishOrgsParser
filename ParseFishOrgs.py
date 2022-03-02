import re
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from Include.getOrgList import getHREF
from Include.writeOutput import CsvWriter

URL = 'http://fishretail.ru/litecat/rybodobyvayushhie_kompanii'
driver = webdriver.Chrome(r"d:/utils/chromedriver_win32/chromedriver.exe")
#wait = WebDriverWait(driver, 500)
#login = "arteemmius@mail.ru"
user_login = "1tradelord@mail.ru"
#password = "jufyre"
user_password = "hacyta"
driver.get(URL)
current_handle = driver.current_window_handle
sleep(2)
#self.driver.find_element_by_xpath("//*[@class='shops-info-region__your-region']/button").click()
#self.driver.find_element_by_link_text("Вся Россия").click()
#elem = driver.find_element_by_xpath("//*")
driver.find_element_by_link_text("Войти на сайт").click()
sleep(2)
user_name = driver.find_element_by_id("u-login")
user_name.send_keys(user_login)
password = driver.find_element_by_id("u-pass")
password.send_keys(user_password)
driver.find_element_by_xpath("//p[@class='i-submit']/input").click()
#elem = []
#elem = driver.find_elements_by_xpath("//div[@class='clear list-style-item ct-green']/h3/a[@target='_blank']")
#elem = elem + driver.find_elements_by_xpath("//div[@class='clear list-style-item']/h3/a[@target='_blank']")
#driver.find_elements_by_xpath("//div[@class='clear list-style-item ct-green']/h3/a[@target='_blank']")[0].click()

#for i in range(0, len(driver.find_elements_by_xpath("//div[@class='clear list-style-item ct-green']/h3/a[@target='_blank']"))):
    #print(driver.find_elements_by_xpath("//div[@class='clear list-style-item ct-green']/h3/a[@target='_blank']")[i].get_attribute("href"))

#org_handle = driver.current_window_handle

#source_code = elem[0].get_attribute("outerHTML")

#print(driver.window_handles)
#print(driver.current_window_handle)

#driver.switch_to.window(current_handle)
#driver.get(driver.find_elements_by_xpath("//div[@class='clear list-style-item ct-green']/h3/a[@target='_blank']")[0].get_attribute("href"))

orgHREF = getHREF()
writeData = CsvWriter()
hrefList = orgHREF.getOrgList()
#1407 complete
for j in range(1407, len(hrefList)):
    orgRegion = ""
    orgDesc = ""
    orgName = ""
    orgAddress = ""
    orgPhone = ""
    orgEmail= ""
    orgURL = ""
    orgTown = ""

    driver.get(hrefList[j])
    orgName = driver.find_element_by_xpath("//h3[@class='list-information']").text
    dataList = driver.find_elements_by_xpath("//ul[@class='vlist vlist_mdash']/li")
    for i in range(0, len(dataList)):
        try:
            if '<strong>Описание:</strong>' in dataList[i].get_attribute("outerHTML"):
                orgDesc = dataList[i].text
        except:
            pass
        try:
            if '<strong>Регион:</strong>' in dataList[i].get_attribute("outerHTML"):
                orgRegion = dataList[i].text
        except:
            pass

    driver.find_element_by_xpath("//div[@class='tabs']/label[@for='tab5']").click()
    sleep(2)
    dataList = driver.find_elements_by_xpath("//ul[@class='vlist vlist_mdash']/li")

    for i in range(0, len(dataList)):
        try:
            if '<strong>Почтовый адрес:</strong>' in dataList[i].get_attribute("outerHTML"):
                orgAddress = dataList[i].text
        except:
            pass
        try:
            if 'Телефон:' in dataList[i].get_attribute("outerHTML"):
                orgPhone = orgPhone + dataList[i].text + ','
        except:
            pass
        try:
            if 'E-mail:' in dataList[i].get_attribute("outerHTML"):
                orgEmail = dataList[i].text
        except:
            pass
        try:
            if 'Сайт:' in dataList[i].get_attribute("outerHTML"):
                orgURL = dataList[i].text
        except:
            pass

    try:
        orgTown = re.search(r"([сгпдх]|нп)\.\s*\b[\w\s]+\b", orgAddress.replace("Почтовый адрес: ", "")).group()
    except:
        pass

    writeData.writeCSV(orgName,orgDesc.replace("Описание: ", ""),orgRegion.replace("Регион: ", ""),orgTown,orgAddress.replace("Почтовый адрес: ", ""),
                       orgPhone[0:len(orgPhone) - 1].replace("Телефон: ", ""),orgEmail.replace("E-mail: ", ""),orgURL.replace("Сайт: ", ""))
    print("org " + hrefList[j] + " processed succesfully")
    sleep(7)

#print(orgAddress.replace("Почтовый адрес: ", ""))
#print(orgPhone[0:len(orgPhone) - 1].replace("Телефон: ", ""))
#print(orgEmail.replace("E-mail: ", ""))
#print(orgURL.replace("Сайт: ", ""))
#print(orgRegion.replace("Регион: ", ""))
#print(orgDesc.replace("Описание: ", ""))
#print(orgTown)

#driver.get('http://fishretail.ru/litecat/voroncov-yu-m-305026')
#driver.get(driver.find_elements_by_xpath("//div[@class='clear list-style-item ct-green']/h3/a[@target='_blank']")[1].get_attribute("href"))


#driver.switch_to.window(current_handle)

#source_code = elem[0].get_attribute("href")
#print(str(len(elem)))
#driver.close()
#print(source_code)
