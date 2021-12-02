from selenium import webdriver
from lxml import etree
from time import sleep
# 实例化一个浏览器对象（传入相应的驱动）
bro = webdriver.Edge(executable_path='./msedgedriver.exe')
# 让浏览器发送一个指定的url请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
# 获取当前页面的源码数据
page_text = bro.page_source
# 解析企业名称
tree = etree.HTML(page_text)
# 解析所有li标签
li_list = tree.xpath('//*[@id="gzlist"]/li')
# 存放企业名称的列表
name_list = []
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    name_list.append(name)
sleep(5)
bro.quit()
print(name_list)



