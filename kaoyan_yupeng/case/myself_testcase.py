#导包
from public_method.assert_screenshot import Assert_Screenshot
from page_object.business_page import Business

class Myself(Assert_Screenshot):

    def test_myself1(self):
        #我模块--退出登录
        driver=self.driver
        Business().login(driver,'zhongyupeng','kaoyan123456')
        text=Business().myself_logout(driver)
        self.assert_equal(driver,text,'未登录')

    def test_myself2(self):
        # 我模块--修改头像--修改考研年份
        driver=self.driver
        Business().login(driver,'zhongyupeng','kaoyan123456')
        text=Business().myself_modify(driver)
        self.assert_equal(driver,text,'2020')

    def test_myself3(self):
        #我模块 - -查看会员中心 - -查看积分 - -查看我的收藏
        driver=self.driver
        Business().login(driver,'zhongyupeng','kaoyan123456')
        text=Business().myself_browse_collection(driver)
        self.assert_equal(driver,text,'我的收藏')

    def test_myself4(self):
        # 我模块--帮助与反馈
        driver=self.driver
        Business().login(driver,'zhongyupeng','kaoyan123456')
        text=Business().myself_help(driver)
        self.assert_equal(driver,text,'如何获取积分？')