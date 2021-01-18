from selenium import webdriver
import time

driver_path = r"C:\Users\nomad\PycharmProjects\kintarou\geckodriver\geckodriver.exe"

# seleniumを使用してgoogle検索画面から検索を実行する
url = "https://www.google.com"
keyword ="スクレイピング"

# driver = webdriver.Firefox()
# プロジェクト上に入れたdriverから起動したい
driver = webdriver.Firefox(executable_path=driver_path)

driver.get(url)
time.sleep(3)

search = driver.find_element_by_name("q")
search. send_keys(keyword)
search.submit()

time.sleep(3)
driver.quit()

'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''