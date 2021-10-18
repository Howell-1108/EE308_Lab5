郑宇晗牛逼
哈哈哈哈哈哈

  def __init__(self):
        self.ua = UserAgent().chrome
        self.url = 'https://blog.csdn.net/api/WritingRank/weekList?'  # ajax 请求网址
        self.header = {
            'Referer': 'https://blog.csdn.net/weixin_39190897',
            "Upgrade-Insecure-Requests": "1",
            'User-Agent': self.ua
        }
        # 配置保存表格的基本
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = 'CSDNTop100信息'
        self.sheet['A1'] = '排名'
        self.sheet['B1'] = '用户名'
        self.sheet['C1'] = '用户头像'
        self.sheet['D1'] = '用户博客网址'
        self.sheet['E1'] = '粉丝数'
        self.sheet['F1'] = '点赞数'
        self.sheet['G1'] = '上周排名'
        self.sheet['H1'] = '博客等级'
        self.sheet['I1'] = '排名时间'

    def __params(self, offset):
        self.offset = offset
        """构造请求参数"""
        self.params = {
            "username": "weixin_39190897",
            "page": str(self.offset),
            "size": "10"
        }
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
2、爬取网址：

    def spider(self):
        """
        构造 多页 爬取
        """
        for i in range(1, 11):
            self.__params(i)
            url = self.url + urlencode(self.params)
            r = requests.get(url, headers=self.header)
            if r.status_code == 200:
                r.encoding = r.apparent_encoding
                yield r.json()
            else:
                print('[info] request error ! the status_code is ' + r.status_code)
            time.sleep(0.5)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
3、分析json包：

 def parse_json(self, r_json):
        """
        根据网站请求返回的json包 进行进一步分析
        """
        # 第一层
        first_data = r_json.get('data')
        if first_data:
            # 第二层
            list_data = first_data.get('list')
            if list_data:  # 判空
                for i in list_data:
                    rank = i.get("ranking")
                    head_image = i.get('avatar')
                    user_nickname = i.get('user_nickname')  # 用户名
                    username = i.get('username')  # 用户id
                    fans_num = i.get('fans_num')  # 粉丝
                    fav_num = i.get('fav_num')  # 获赞
                    last_rank = i.get('last_ranking')  # 上周排名
                    leave = i.get('profile_level').get('level')  # 博客等级
                    if rank and head_image and user_nickname and user_nickname and username and fans_num \
                            and fav_num and last_rank and leave:
                        # 这里保存数据 只是为了方便转换其他保存格式  仅仅是保存excel中用到列表
                        yield {
                            'rank': rank,
                            'user_nickname': user_nickname,
                            'head_image': head_image,
                            'username': 'https://blog.csdn.net/' + username,
                            'fans_num': fans_num,
                            'fav_num': fav_num,
                            'last_rank': last_rank,
                            'leave': leave
                        }
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
4、下载保存excel表格

    def down(self, item):
        """保存至excel表格"""
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  #  时间
        leave_list = []
        for value in item.values():
            leave_list.append(value)
        leave_list.append(now_time)
        self.sheet.append(leave_list)
1
2
3
4
5
6
7
8
5、完整脚本：

# -*- coding :  utf-8 -*-
import requests
from urllib.parse import urlencode
from fake_useragent import UserAgent
import time
from openpyxl import Workbook

class CSDNSpider(object):
    """
     爬取csdn top 100 的各种信息
     url = 'https://blog.csdn.net/rank/writing_rank'
     ajax方式
    """

    def __init__(self):
        self.ua = UserAgent().chrome
        self.url = 'https://blog.csdn.net/api/WritingRank/weekList?'  # ajax 请求网址
        self.header = {
            'Referer': 'https://blog.csdn.net/weixin_39190897',
            "Upgrade-Insecure-Requests": "1",
            'User-Agent': self.ua
        }
        # 配置保存表格的基本
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = 'CSDNTop100信息'
        self.sheet['A1'] = '排名'
        self.sheet['B1'] = '用户名'
        self.sheet['C1'] = '用户头像'
        self.sheet['D1'] = '用户博客网址'
        self.sheet['E1'] = '粉丝数'
        self.sheet['F1'] = '点赞数'
        self.sheet['G1'] = '上周排名'
        self.sheet['H1'] = '博客等级'
        self.sheet['I1'] = '排名时间'

    def __params(self, offset):
        self.offset = offset
        """构造请求参数"""
        self.params = {
            "username": "weixin_39190897",
            "page": str(self.offset),
            "size": "10"
        }

    def spider(self):
        """
        构造 多页 爬取
        """
        for i in range(1, 11):
            self.__params(i)
            url = self.url + urlencode(self.params)
            r = requests.get(url, headers=self.header)
            if r.status_code == 200:
                r.encoding = r.apparent_encoding
                yield r.json()
            else:
                print('[info] request error ! the status_code is ' + r.status_code)
            time.sleep(0.5)

    def parse_json(self, r_json):
        """
        根据网站请求返回的json包 进行进一步分析
        """
        # 第一层
        first_data = r_json.get('data')
        if first_data:
            # 第二层
            list_data = first_data.get('list')
            if list_data:  # 判空
                for i in list_data:
                    rank = i.get("ranking")
                    head_image = i.get('avatar')
                    user_nickname = i.get('user_nickname')  # 用户名
                    username = i.get('username')  # 用户id
                    fans_num = i.get('fans_num')  # 粉丝
                    fav_num = i.get('fav_num')  # 获赞
                    last_rank = i.get('last_ranking')  # 上周排名
                    leave = i.get('profile_level').get('level')  # 博客等级
                    if rank and head_image and user_nickname and user_nickname and username and fans_num \
                            and fav_num and last_rank and leave:
                        # 这里保存数据 只是为了方便转换其他保存格式  仅仅是保存excel中用到列表
                        yield {
                            'rank': rank,
                            'user_nickname': user_nickname,
                            'head_image': head_image,
                            'username': 'https://blog.csdn.net/' + username,
                            'fans_num': fans_num,
                            'fav_num': fav_num,
                            'last_rank': last_rank,
                            'leave': leave
                        }

    def down(self, item):
        """保存至excel表格"""
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        leave_list = []
        for value in item.values():
            leave_list.append(value)
        leave_list.append(now_time)
        self.sheet.append(leave_list)

    def main(self):
        """调用函数"""
        print('The spider is start!')
        for content in self.spider():
            for item in self.parse_json(content):
                self.down(item)

        self.workbook.save(filename='CSDNTop100.xlsx')
        self.workbook.close()
        print('The CSDNTop100 spider is over!')


a = CSDNSpider()
a.main()