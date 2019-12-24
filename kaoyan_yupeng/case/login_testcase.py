#导包
from public_method.assert_screenshot import Assert_Screenshot
from page_object.business_page import Business

class Login(Assert_Screenshot):

    def test_login_succed(self):
        #登录成功
        driver=self.driver
        Business().login(driver,'zhongyupeng','kaoyan123456')
        text=Business().return_text(driver)
        self.assert_equal(driver,text,'zhongyupeng')












