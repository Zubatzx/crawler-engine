from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import os
import platform
import time

class Selenium:
    max_try_count = 3
    implicit_wait_time = 1  # implicit wait will tell the web driver to wait for certain amount of time before it throws a 'No Such Element Exception'

    def __init__(self):
        operating_system = platform.system().lower()
        chrome_driver_path = ""
        download_default_directory = ""

        # Setting lokasi chromium
        if operating_system == "linux":
            chrome_driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chromedriver")
            # download_default_directory = "/home/" + os.getlogin() + "/Downloads/"
        elif operating_system == "windows":
            # Lokasi chromedriver ada di folder project
            chrome_driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chromedriver.exe")
            # download_default_directory = "C:\\Users\\" + os.getlogin() + "\\Downloads\\"

        # Atur settingan di chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument("user-data-dir=C:\\Users\\" + os.getlogin() + "\\Desktop\\auto-purchase-crawler\\cookie") # berguna untuk ambil data cookie dari suatu tempat
        chrome_options.add_argument("--disable-notifications") # disable notification di chrome
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--disable-gpu')
        # prefs = {'download.default_directory' : download_default_directory} # set default download path
        # chrome_options.add_experimental_option("prefs", prefs)

        # SETTING WAJIB APABILA RUN SEBAGAI DOCKER IMAGE
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("window-size=1400,2100")
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--disable-gpu')
        # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
        # chrome_options.add_argument('user-agent={0}'.format(user_agent))

        # self.display = Display(visible=0, size=(1920, 1080))
        # self.display.start()
        self.driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
        self.driver.implicitly_wait(self.implicit_wait_time)

    def Close(self):
        self.driver.close()
        self.driver.quit()
        # self.display.popen.terminate()
        # self.display.stop()

    def Sleep(self, sec):
        print("Delay for", str(sec), "second")
        time.sleep(sec)

    def ScrollTo(self, scroll_height):
        self.driver.execute_script("window.scrollTo(0," + str(scroll_height) + ")")

    def LoadURL(self, url):
        print("Load:", url)
        self.driver.get(url)

    def GetCurrentUrl(self):
        print("Current Url:", self.driver.current_url)
        return self.driver.current_url

    def GetElemByXpath(self, xpath):
        try:
            elem = self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            elem = None
            print('Element not found')
        return elem

    def GetElemsByXpath(self, xpath):
        try:
            elems = self.driver.find_elements_by_xpath(xpath)
        except Exeption as e:
            elems = None
            print('Elements not found')
        return elems

    #Single Element
    def ElemText(self, xpath):
        elem = self.GetElemByXpath(xpath)
        if elem is not None:
            print('Extracted text:', elem.text)
            print('From xpath:', xpath)
            return elem.text
        else:
            print('Element is None')
            return None
    
    def ElemTextByAttribute(self, xpath, attribute):
        elem = self.GetElemByXpath(xpath)
        if elem is not None:
            print('Extracted text:', elem.get_attribute(attribute))
            print('From xpath:', xpath)
            print('With attribute:', attribute)
            return elem.get_attribute(attribute)
        else:
            print('Element is None')
            return None

    def ClickElem(self, xpath):
        elem = self.GetElemByXpath(xpath)
        if elem is not None:
            print('Click element with xpath:', xpath)
            elem.click()

    def ClearElem(self, xpath):
        elem = self.GetElemByXpath(xpath)
        if elem is not None:
            print('Clear element with xpath:', xpath)
            elem.send_keys(Keys.CONTROL + "a")
            elem.send_keys(Keys.DELETE)

    def InputToElem(self, xpath, keyword):
        elem = self.GetElemByXpath(xpath)
        if elem is not None:
            print('Input', keyword, 'into element with xpath:', xpath)
            elem.send_keys(keyword)

    #Multiple Element
    def CountElems(self, xpath):
        elems = self.GetElemsByXpath(xpath)
        return len(elems)

    def ElemsText(self, xpath):
        elems = self.GetElemsByXpath(xpath)
        if elems is not None:
            elemsText = []
            for elem in elems:
                elemsText.append(elem.text)

            return elemsText
        else:
            print('Elements is None')
            return None

    def ElemsTextByAttribute(self, xpath, attribute):
        elems = self.GetElemsByXpath(xpath)
        if elems is not None:
            elemsText = []
            for elem in elems:
                print('Extracted text:', elem.get_attribute(attribute))
                print('From xpath:', xpath)
                print('With attribute:', attribute)
                elemsText.append(elem.get_attribute(attribute))

            return elemsText
        else:
            print('Elements is None')
            return None

    def SwitchFrame(self, xpath):
        elem = self.GetElemByXpath(xpath)
        if elem is not None:
            print('Switch frame with xpath:', xpath)
            self.driver.switch_to_frame(elem)
