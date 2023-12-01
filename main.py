from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from fake_useragent import UserAgent
import time


myUsername = "Gamarezing"
myPassword = "automategamarezing23"
channelUrl = "https://www.youtube.com/@gamarezing"
channelDescription = "Channel that show most historic momment in gaming"

UA = UserAgent()
userAgent = UA.random

options = Options()
options.add_experimental_option("detach",True)
options.add_argument(f'user-agent={userAgent}')

# Here you set the path of the profile ending with User Data not the profile folder
options.add_argument("user-data-dir=C:\\Users\\AGYEMAN-PC\\AppData\\Local\\Microsoft\\Edge\\User Data")
options.add_argument("profile-directory=Default")

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),
                        options=options)
time.sleep(4)
driver.get("https://www.like4like.org/login/")
def log_in():
    username_input = driver.find_element(by=By.ID,value="username")
    username_input.clear()
    username_input.send_keys(myUsername)

    password_input = driver.find_element(by=By.ID,value="password")
    password_input.clear()
    password_input.send_keys(myPassword)

    login_button = driver.find_element(by=By.XPATH,value='//span[contains(@class, "button") and contains(@class, "orange") and contains(@class, "cursor") and contains(@class, "medium")]')
    login_button.click()
    time.sleep(2)


def getting_things_ready_for_process():
    # Getting page after login page and going to page to help get credits
    WebDriverWait(driver=driver,timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    driver.get("https://www.like4like.org/#social-media-platform-list")
    freeCredit_button = driver.find_element(by=By.XPATH,value='//li[contains(@class, "dropdown") and contains(@class, "text-center") and contains(@class, "menu-features")]')
    freeCredit_button.click()

    #Getting free credits page and select youtube subscribers has the preferred option
    WebDriverWait(driver=driver,timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    driver.get("https://www.like4like.org/earn-credits.php")
    youtubeSubscribers_option = driver.find_element(by=By.XPATH,value="//option[contains(@value, 'youtubes')]")
    youtubeSubscribers_option.click()
    WebDriverWait(driver=driver,timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")



def get_credits():
    while True:
        time.sleep(3)
        
        WebDriverWait(driver=driver,timeout=15).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        getCredit_button = driver.find_element(by=By.XPATH,value='//a[contains(@class, "pulse-checkBox") and contains(@class, "earn_pages_button") and contains(@class, "cursor")]')
        getCredit_button.click()
        WebDriverWait(driver=driver,timeout=15).until(      
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
            
        subscribe_button = driver.find_element(by=By.XPATH,value='//button[contains(@class, "yt-spec-button-shape-next") and contains(@class, "yt-spec-button-shape-next--filled") and contains(@class, "yt-spec-button-shape-next--size-m") and contains(@class, "yt-spec-button-shape-next--mono")]')
        subscribe_button.click()
        time.sleep(3)
        
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        confirm_button = driver.find_element(by=By.XPATH,value="//a[contains(@class, 'cursor') and contains(@class, 'pulse-checkBox')]")
        confirm_button.click()

# log_in()   
getting_things_ready_for_process()
get_credits()

