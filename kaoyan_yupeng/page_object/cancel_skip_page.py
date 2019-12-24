from time import sleep

class Cancel_Skip():

    def cancel_skip(self,driver):
        # 取消
        sleep(3)
        try:
            driver.find_element_by_id('android:id/button2').click()
        except:
            pass

        # 跳过
        sleep(3)
        try:
            driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()
        except:
            pass

        # 不重置跳到登录页面
        try:
            driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
            driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
        except:
            pass