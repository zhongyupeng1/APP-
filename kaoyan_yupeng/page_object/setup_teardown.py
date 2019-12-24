import unittest
from time import sleep
from page_object.capability_setting import Caps
from page_object.cancel_skip_page import Cancel_Skip
from page_object.driver_romote import Driver_Romote

class Setup_Teardown(unittest.TestCase):

    def setUp(self) -> None:
        # capability配置信息
        caps = Caps().cap_setting()

        # 启动
        self.driver = Driver_Romote().driver_romote(caps)

        # 取消和跳过
        Cancel_Skip().cancel_skip(self.driver)

    def tearDown(self) -> None:
        # 暂停3秒后退出
        sleep(1)
        self.driver.quit()