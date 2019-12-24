#定义一个字典存放capability配置信息
class Caps():
    def cap_setting(self,noReset=False):
        caps = {
          "platformName": "Android",
          "platformVerison": "4.4.2",
          "deviceName": "127.0.0.1:62001",
          "app": r"C:\Users\zhong\Desktop\APPinstall\kaoyan3.1.0.apk",
          "appPackage": "com.tal.kaoyan",
          "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
          "noReset": noReset,
          #设置键盘
          "unicodeKeyboard": "True",
          "resetKeyboard" : "True"
        }
        return caps