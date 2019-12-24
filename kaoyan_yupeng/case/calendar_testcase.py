#导包
from public_method.assert_screenshot import Assert_Screenshot
from page_object.business_page import Business

class Calendar(Assert_Screenshot):

    def test_calendar1(self):
        #日历--添加学习任务
        driver=self.driver
        Business().login(driver, 'zhongyupeng', 'kaoyan123456')
        text=Business().calendar_task(driver)
        self.assert_equal(driver, text, '做英语阅读')

    def test_calendar2(self):
        #日历--浏览、评论文章
        driver=self.driver
        Business().login(driver, 'zhongyupeng', 'kaoyan123456')
        text=Business().calendar_comment(driver)
        self.assert_equal(driver, text, '这文章写的真好')

    def test_calendar3(self):
        #日历模块---史纲冲刺练习
        driver=self.driver
        Business().login(driver, 'helo1234', 'helo1234')
        text=Business().calendar_practice(driver)
        self.assert_equal(driver, text, '练习报告-每日一练')

