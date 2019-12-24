from public_method.random_number import Random_Number
from time import sleep

class Business():

    def login(self,driver,username,password):
        # 登录
        login_usernameid='com.tal.kaoyan:id/login_email_edittext'
        login_passwordid='com.tal.kaoyan:id/login_password_edittext'
        login_buttonid='com.tal.kaoyan:id/login_login_btn'
        driver.find_element_by_id(login_usernameid).send_keys(username)
        driver.find_element_by_id(login_passwordid).send_keys(password)
        driver.find_element_by_id(login_buttonid).click()

    def return_text(self,driver):
        #返回账号text
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
        text=driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').text
        return text

    def registerd(self,driver):
        #注册
        driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
        driver.find_elements_by_id('com.tal.kaoyan:id/item_image')[3].click()
        driver.find_element_by_id('com.tal.kaoyan:id/save').click()
        username = Random_Number().random_username()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)
        password = Random_Number().random_password()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)
        email = Random_Number().random_email()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)
        # 判断用户名输入是否正确(用户名已注册或格式错误，则重新输入)
        text = driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').text
        while (text != username):
            username = Random_Number().random_username()
            driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)
            driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').click()
            text = driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').text
        driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
        driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
        driver.find_element_by_xpath('//*[@text="湖北"]').click()
        driver.find_element_by_xpath('//*[@text="华中师范大学"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
        driver.find_element_by_xpath('//*[@text="法学"]').click()
        driver.find_element_by_xpath('//*[@text="社会学"]').click()
        driver.find_element_by_xpath('//*[@text="社会经济学"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()
        return username

    def calendar_task(self,driver):
        #日历模块---添加学习任务
        sleep(2)
        driver.tap([(0,38),(720,478)], 100)
        sleep(2)
        driver.find_element_by_id('com.tal.kaoyan:id/task_no_task').click()
        driver.find_element_by_id('com.tal.kaoyan:id/btnHot4').click()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_date_addtask_selectdate_commitbtn').click()
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        driver.find_element_by_id('com.tal.kaoyan:id/home_task_select').click()
        driver.find_element_by_id('com.tal.kaoyan:id/task_info_showall_text').click()
        driver.find_element_by_id('com.tal.kaoyan:id/home_task_title').click()
        text=driver.find_element_by_id('com.tal.kaoyan:id/tvTitle').text
        #删除任务
        sleep(2)
        driver.find_element_by_id('com.tal.kaoyan:id/ivDelete').click()
        driver.find_element_by_id('com.tal.kaoyan:id/btnDeleteAllTask').click()
        return text

    def calendar_comment(self,driver):
        #日历模块---浏览、评论文
        sleep(5)
        driver.tap([(0, 38), (720, 478)], 100)
        sleep(2)
        driver.swipe(100, 100, 100, 1000, 4000)
        sleep(2)
        driver.swipe(360, 1045, 360, 200, 4000)
        sleep(2)
        driver.find_element_by_xpath('//*[@text="政治押题卷重点：这几道题所有政治押题卷都出现了！我猜它一定会考！"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_inquiry_addComment').click()
        driver.find_element_by_id('com.tal.kaoyan:id/create_comment_content_edittext').send_keys('这文章写的真好')
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        sleep(2)
        for i in range(0,4):
            driver.swipe(360, 1200, 360, 10, 4000)
            sleep(2)
        text = driver.find_element_by_id('com.tal.kaoyan:id/comment_itemlayout_commentcontent').text
        return text

    def calendar_practice(self,driver):
        #日历模块---史纲冲刺练习
        sleep(3)
        driver.tap([(0, 38), (720, 478)], 100)
        driver.find_element_by_xpath('//*[@text="每日练"]').click()

        driver.find_elements_by_xpath('//*[@class="android.view.View" and@content-desc="23Dec. Link"]')[0].click()

        text = driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_Title').text
        if text == "练习报告-每日一练":  # 做题-每日一练--->没做过题
            # 做过题--直接判断
            return text
        else:
            # 没做过题，先做题--再判断
            driver.find_elements_by_class_name('android.view.View')[-1].click()
            driver.find_elements_by_class_name('android.view.View')[-1].click()
            driver.find_elements_by_class_name('android.view.View')[-1].click()
            driver.find_elements_by_class_name('android.view.View')[-1].click()
            # 提交试卷
            driver.find_elements_by_class_name('android.view.View')[-1].click()
            sleep(2)
            text = "练习报告-每日一练"
            return text

    def college_fractionalline(self,driver):
        #院校模块--查看院校信息--查看分数线--加入、退出讨论组--退出
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_info').click()
        driver.find_element_by_xpath('//*[@text="院校资讯"]').click()
        driver.find_element_by_xpath('//*[@text="招生信息"]').click()
        driver.find_element_by_xpath('//*[@text="招生简章"]').click()
        driver.find_element_by_xpath('//*[@text="专业目录"]').click()
        driver.find_element_by_xpath('//*[@text="报录分析"]').click()
        driver.find_element_by_xpath('//*[@text="学校论坛"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/new_item_school_scoreline_tip').click()
        text=driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_Title').text
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_leftbutton_image').click()
        #加入、退出讨论组（被禁止加入）
        # driver.find_element_by_id('com.tal.kaoyan:id/new_item_school_chat_headers').click()
        # driver.find_element_by_xpath('//*[@text="设置"]').click()
        # driver.find_element_by_xpath('//*[@text="退出群聊"]').click()
        # driver.find_element_by_xpath('//*[@text="确定"]').click()
        return text

    def college_professional_information(self,driver):
        #院校模块--查看专业信息--查看文章正文
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_info').click()
        driver.find_element_by_xpath('//*[@index="1" and @class="android.widget.TextView"]').click()
        driver.find_element_by_xpath('//*[@text="报录分析"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_leftbutton_image').click()
        driver.find_element_by_xpath('//*[@text="专业排名"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_leftbutton_image').click()
        driver.find_element_by_xpath('//*[@text="专业经验"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_leftbutton_image').click()
        driver.find_element_by_xpath('//*[@text="专业书籍"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_leftbutton_image').click()
        driver.find_element_by_id('com.tal.kaoyan:id/news_item_layout_newstitle_textview').click()
        text=driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_Title').text
        return text

    def bbs_hot(self, driver,comment='一起加油哈'):
        # 论坛--24小时热门--帖子回复
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()
        driver.find_element_by_xpath('//*[@text="20考研人注意了，这份准考证打印攻略请收下！"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_threaddetail_commenttip_btn').click()
        driver.find_element_by_id('com.tal.kaoyan:id/createthread_content_edittext').send_keys(comment)
        driver.find_element_by_id('com.tal.kaoyan:id/createthread_title_send').click()
        sleep(3)
        text = driver.find_elements_by_id('com.tal.kaoyan:id/post_item_text')[-1].text
        return text

    def bbs_attention(self, driver):
        # 论坛--我的关注--浏览帖子
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()
        driver.find_element_by_xpath('//*[@text="我的关注"]').click()
        driver.find_element_by_xpath('//*[@text="2020年考研"]').click()
        text = driver.find_element_by_id('com.tal.kaoyan:id/forum_block_view_name').text
        driver.tap([(0, 38), (720, 478)], 100)
        driver.swipe(360, 1045, 360, 200, 5000)
        driver.swipe(360, 1045, 360, 200, 5000)
        driver.swipe(360, 1045, 360, 200, 5000)
        return text

    def bbs_attention_more(self, driver):
        # 论坛--我的关注--关注更多--关注、取消关注
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()
        driver.find_element_by_xpath('//*[@text="我的关注"]').click()
        #关注
        driver.find_element_by_xpath('//*[@text="关注更多"]').click()
        driver.find_element_by_xpath('//*[@text="公共课"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/forum_block_view_follow').click()
        driver.find_element_by_xpath('//*[@text="完成"]').click()
        text=driver.find_element_by_id('com.tal.kaoyan:id/forum_block_view_name').text
        #取消关注
        driver.find_element_by_xpath('//*[@text="关注更多"]').click()
        driver.find_element_by_xpath('//*[@text="公共课"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/forum_block_view_follow').click()
        driver.find_element_by_xpath('//*[@text="完成"]').click()
        return text


    def myself_logout(self, driver):
        # 我模块--退出登录
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
        driver.find_element_by_xpath('//*[@text="确定"]').click()
        text=driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').text
        return text

    def myself_modify(self, driver):
        # 我模块--修改头像--修改考研年份
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
        #点击头像
        driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_userheader').click()
        #点击换头像
        driver.find_element_by_id('com.tal.kaoyan:id/activity_myinfo_header_relativelayout').click()
        driver.find_elements_by_id('com.tal.kaoyan:id/item_image')[4].click()
        driver.find_element_by_id('com.tal.kaoyan:id/save').click()
        #修改考研年份
        driver.find_element_by_id('com.tal.kaoyan:id/activity_myinfo_year_relativelayout').click()
        driver.find_element_by_xpath('//*[@index="6"]').click()
        text=driver.find_element_by_id('com.tal.kaoyan:id/activity_myinfo_yeartextview').text
        return text

    def myself_clearcache(self, driver):
        # 我模块--清理缓存
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
        #设置
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        driver.find_element_by_id('com.tal.kaoyan:id/setting_clearcache_relativelayout').click()
        text=driver.find_element_by_id('com.tal.kaoyan:id/setting_cachesize_textview').text
        return text

    def myself_browse_collection(self, driver):
        # 我模块--查看会员中心--查看积分--查看我的收藏
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
        driver.find_element_by_xpath('//*[@text="会员中心"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_leftbutton_image').click()
        driver.find_element_by_xpath('//*[@text="发帖，回复，赚积分"]').click()
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_leftbutton_image').click()
        driver.find_element_by_xpath('//*[@text="我的收藏"]').click()
        text=driver.find_element_by_id('com.tal.kaoyan:id/activity_mycollection_titletext_textview').text
        driver.find_element_by_id('com.tal.kaoyan:id/activity_mycollection_leftbutton_image').click()
        return text

    def myself_help(self, driver):
        # 我模块--帮助与反馈
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
        driver.find_element_by_xpath('//*[@text="帮助与反馈"]').click()
        driver.find_element_by_xpath('//*[@text="如何获取积分？"]').click()
        text='如何获取积分？'
        return text

