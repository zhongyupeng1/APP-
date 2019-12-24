#导包
from page_object.business_page import Business
from public_method.assert_screenshot import Assert_Screenshot

class Registered(Assert_Screenshot):

    def test_registered_scceed(self):
        # 注册成功
        driver = self.driver
        username=Business().registerd(driver)
        text = Business().return_text(driver)
        self.assert_equal(driver, text, username)


