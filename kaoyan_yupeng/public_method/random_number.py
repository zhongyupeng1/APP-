import random,string

class Random_Number():

    def random_username(self):
        #用户名必须由3-15个字符或者2-7个汉字组成
        if random.randint(0,1)==0:
            # 生成3-15个随机字母
            src_letters = string.ascii_letters  # 所有字母
            letters_num = random.randint(3,15)
            username = random.sample(src_letters, letters_num)
            username = ''.join(username)
        else:
            username=''
            for i in range(0,random.randint(2,7)):
                # 生成随机中文
                head = random.randint(0xb0, 0xf7)
                body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
                val = f'{head:x}{body:x}'
                random_chinese = bytes.fromhex(val).decode('gb2312')
                username+=random_chinese
        return username

    def random_password(self):
        # 密码至少6位-----到10位
        password = []
        for i in range(0, random.randint(7, 10)):
            password.append(random.randint(0, 9))
        password = [str(x) for x in password]
        password=''.join(password)
        return password

    def random_email(self):
        # 邮箱地址要合法
        digit = str(random.random())[2:8]
        list0 = [digit]
        list1 = ['@qq', '@sina', '@163', '@263']
        list2 = ['.cn', '.com']
        email=random.choice(list0)+random.choice(list1)+random.choice(list2)
        return email

a=Random_Number()
for i in range(2,100):
    print(a.random_email())
