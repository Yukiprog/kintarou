from selenium import webdriver
import time

def execute():
    # Selenum用ドライバ格納パス
    driver_path = r"C:\Users\yuki\PycharmProjects\kintarou\geckodriver\geckodriver.exe"
    enter_company = ""
    enter_username = ""
    enter_password = ""


    # seleniumを使用してgoogle検索画面から検索を実行する
    url = "https://www.kinta.ne.jp/kinta2/web_sp/login.aspx"

    # browser = webdriver.Firefox()
    # プロジェクト上に入れたdriverから起動したい
    browser = webdriver.Firefox(executable_path=driver_path)
    browser.get(url)

    enter_info(enter_company,enter_username,enter_password)

    company = browser.find_element_by_id('txtCode')
    username = browser.find_element_by_id('txtEmpCode')
    password = browser.find_element_by_id('txtPw')

    company.send_keys(enter_company)
    username.send_keys(enter_username)
    password.send_keys(enter_password)

    browser.close()

def enter_info(enter_company,enter_username,enter_password):
    from getpass import getpass
    enter_company = input("comapany name is:")
    enter_username = input("username is:")
    enter_password = getpass("password is:")
