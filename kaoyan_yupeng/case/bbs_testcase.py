#导包
from public_method.assert_screenshot import Assert_Screenshot
from page_object.business_page import Business

class BBS(Assert_Screenshot):

    def test_bbs1(self):
        # 论坛--24小时热门--帖子回复
        driver=self.driver
        Business().login(driver, 'zhongyupeng', 'kaoyan123456')
        text=Business().bbs_hot(driver)
        self.assert_equal(driver, text, '一起加油哈')

    def test_bbs2(self):
        # 论坛--我的关注--浏览帖子
        driver=self.driver
        Business().login(driver, 'zhongyupeng', 'kaoyan123456')
        text=Business().bbs_attention(driver)
        self.assert_equal(driver, text, '2020年考研')

    def test_bbs3(self):
        # 论坛--我的关注--关注更多--关注、取消关注
        driver=self.driver
        Business().login(driver, 'zhongyupeng', 'kaoyan123456')
        text=Business().bbs_attention_more(driver)
        self.assert_equal(driver, text, '政治')

    def test_bbs4(self):
        # 论坛--24小时热门--帖子回复
        driver=self.driver
        Business().login(driver, 'zhongyupeng', 'kaoyan123456')
        text=Business().bbs_hot(driver,comment='滴滴滴打卡')
        self.assert_equal(driver, text, '滴滴滴打卡')