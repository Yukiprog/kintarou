from selenium import webdriver

def execute():
    # Selenum用ドライバ格納パス
    driver_path = r"C:\Users\yuki\PycharmProjects\kintarou\geckodriver\geckodriver.exe"
    enter_data = ["", "", ""]

    # seleniumを使用してgoogle検索画面から検索を実行する
    url = "https://www.kinta.ne.jp/kinta2/web_sp/login.aspx"

    # browser = webdriver.Firefox()
    # プロジェクト上に入れたdriverから起動したい
    browser = webdriver.Firefox(executable_path=driver_path)
    browser.get(url)

    # enter_info(enter_data)

    company = browser.find_element_by_id('txtCode')
    username = browser.find_element_by_id('txtEmpCode')
    password = browser.find_element_by_id('txtPw')

    company.send_keys(enter_data[0])
    username.send_keys(enter_data[1])
    password.send_keys(enter_data[2])

    password.submit()

    # time.sleep(5)
    # browser.close()