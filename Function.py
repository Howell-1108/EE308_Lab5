hhhhhhhhhhhhhhhhhhh
陈震朔牛逼
哈哈哈哈哈哈

#-*- coding:utf-8 -*-
import sys
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
from article import CsdnArticle
 
reload(sys)
sys.setdefaultencoding('utf-8')
 
class CsdnCrawler(object):
	#默认访问我的博客
	def __init__(self, author = 'whiterbear'):
		self.author = author
		self.domain = 'http://blog.csdn.net/'
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
		#存储文章对象数组
		self.articles = []
	
	#给定url，得到所有的文章lists
	def getArticleLists(self, url= None):
		req = urllib2.Request(url, headers=self.headers)
		response = urllib2.urlopen(req)
 
		soup = BeautifulSoup(''.join(response.read()))
		listitem =  soup.find(id='article_list').find_all(attrs={'class':r'list_item article_item'})
		#链接的正则表达式，可以匹配链接
		href_regex = r'href="(.*?)"'
		for i,item in enumerate(listitem):
			enitem = item.find(attrs={'class':'link_title'}).contents[0].contents[0]
			href = re.search(href_regex,str(item.find(attrs={'class':'link_title'}).contents[0])).group(1)
			#我们将获取的一篇文章信息封装成一个对象，然后存入数组中
			art = CsdnArticle()
			art.author = self.author
			art.title = enitem.lstrip()
			art.href = (self.domain + href[1:]).lstrip()
			self.articles.append(art)
 
 
	def getPageLists(self, url= None):
		url = 'http://blog.csdn.net/%s?viewmode=list'%self.author
		req = urllib2.Request(url, headers=self.headers)
		response = urllib2.urlopen(req)
 
		soup = BeautifulSoup(''.join(response.read()))
		num_regex = '[1-9]\d*'
		pagelist = soup.find(id='papelist')
		self.getArticleLists(url)
		
		#如果该作者博客多，有分页的话
		if pagelist:
			pagenum = int(re.findall(num_regex, pagelist.contents[1].contents[0])[1])
			for i in range(2, pagenum + 1):
				self.getArticleLists(self.domain + self.author + '/article/list/%s'%i)
		
 
	def mytest(self):
		for i,url in enumerate(self.articles):
			print i,url
 
def main():
	#可以将pongba换成你的博客名，也可以不填，为空，这样默认是访问我的博客
	csdn = CsdnCrawler(author='pongba')#'pongba'
	csdn.getPageLists()
	csdn.mytest()
 
if __name__ == '__main__':
	main()<span style="font-family:Verdana;font-size:18px;">
</span>