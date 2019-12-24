from appium import webdriver

class Driver_Romote():

    def driver_romote(self,caps):
        #连接打开远程设备
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(5)
        return driver