#导包
from public_method.assert_screenshot import Assert_Screenshot
from page_object.business_page import Business

class College(Assert_Screenshot):

    def test_fractionalline(self):
        # 院校模块--查看信息--查看分数线--加入、退出讨论组--退出
        driver=self.driver
        Business().login(driver, 'zhongyupeng', 'kaoyan123456')
        text=Business().college_fractionalline(driver)
        self.assert_equal(driver, text, '分数线')

    def test_professional_information(self):
        # 院校模块--查看专业信息--查看文章正文
        driver=self.driver
        Business().login(driver, 'zhongyupeng', 'kaoyan123456')
        text=Business().college_professional_information(driver)
        self.assert_equal(driver, text, '正文')