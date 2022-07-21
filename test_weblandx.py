from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pytest
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])

@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://landx.id/')
    yield driver
    # driver.quit()

# scenario 1 test pindah ke section proyek yang sedang berlangsung
def test_pendanaansection(setup):
# pindah ke section proyek
    pindahsection = setup.find_element(By.XPATH, '//*[@id="ongoing-projects"]')
    action = ActionChains(setup)
    action.move_to_element(pindahsection).perform()
    print("berhasil pindah ke section proyek")
    time.sleep(5)

# masuk ke halaman semua proyek
    buttonSemuaProject = setup.find_element(By.XPATH, '//*[@id="ongoing-projects"]/div[3]/div/a/button').click()
    time.sleep(10)
    print("berhasil masuk ke halaman semua proyek")
    setup.execute_script("window.scrollBy(0,500)","")

#  klik button beli pada salah satu proyek
    setup.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/button').click()
    time.sleep(10)
    print("berhasil pilih 1 proyek")

# klik button SHOW PROSPEKTUS
    setup.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/div[1]/div[2]/div[2]/div[8]/div[2]/button').click()

    jumlahgambar = setup.find_elements(By.CLASS_NAME, "page")
    time.sleep(20)
    print(len(jumlahgambar))
    jumlahgmbr =  len(jumlahgambar)
    time.sleep(5)
    for i in range(1, jumlahgmbr+1):
        downloadgmbr = setup.find_element(By.XPATH, '//*[@id="page'+str(i)+'"]')
        # print('masukpage')
        action.move_to_element(downloadgmbr)
        action.context_click(downloadgmbr).perform()
        time.sleep(1)
        pyautogui.press('down')
        pyautogui.press('enter')
        # print("bisaperform")
        time.sleep(20)
        pyautogui.press('enter')
        time.sleep(20)
        print("download ke -"+str(i))
    
    setup.refresh()
    title =setup.title
    assert title == "Punya bisnis Ayam Tempong Bu Sri modal 1 juta"



