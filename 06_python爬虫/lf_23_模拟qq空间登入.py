from selenium import webdriver
from selenium.webdriver import ActionChains
# from selenium.webdriver import EdgeOptions
import requests
from lxml import etree
from time import sleep
import os

# 如何实现selenium不被检测到的风险
# option = EdgeOptions()
# option.add_experimental_option('excludeSwitches',['enable-automatioan'])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'
}

bro = webdriver.Edge(executable_path='./msedgedriver.exe')
bro.get('https://qzone.qq.com/')
# 在iframe标签下需要切换作用域,switch_to.frame(iframe的id)
bro.switch_to.frame('login_frame')
# 进行标签定位，定位到账号密码登入
a_tag = bro.find_element_by_xpath('//*[@id="switcher_plogin"]')
# 点击标签
a_tag.click()

# 找到账号输入标签和密码输入标签
userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')

# 输入账号密码
userName_tag.send_keys('772404387')
password_tag.send_keys('LiFei18573743375')

# 定位到登入按键，点击登入按键
login_btn = bro.find_element_by_id('login_button')
login_btn.click()

# 更换作用域，验证页面，定位到滑块标签
iframe = bro.find_element_by_xpath('//iframe')  # 找到“嵌套”的iframe，开头//表示从当前节点寻找所有的后代元素，当前在iframe 需要往下嵌套的iframe
bro.switch_to.frame(iframe)  # 切换到iframe
slideBlock_tag = bro.find_element_by_xpath('//*[@id="slideBlock"]')
# slideBlock_tag = bro.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]/img')
print('找到滑块了')
# 动作链
action = ActionChains(bro)
# 点击并保持
action.click_and_hold(slideBlock_tag).perform()
# 进行滑动并执行动作链--为了体现人慢慢滑动，分五次进行滑动(到缺口距离为171)
for i in range(5):
    action.move_by_offset(34, 0).perform()
    sleep(1)
# 释放动作链
action.release()
# 获取所有的动态信息
page_text = bro.page_source
tree = etree.HTML(page_text)
# 获取所有li标签
li_list = tree.xpath('//*[@id="host_home_feeds"]/li')
# 存放文字和图片的文件夹
if not os.path.exists('./qqKongJiangLibs'):
    os.mkdir('./qqKongJiangLibs')
for li in li_list:
    time = li.xpath('.//div[@class="info-detail"]/span/text()')[0]
    text_content = li.xpath('./div[2]/div/div/text()')[0]
    pic_url = li.xpath('./div[2]/div/div/img/@src')[0]
    pic_detail = requests.get(url=pic_url,headers=headers).content
    text_path_name = './qqKongJiangLibs/' + time
    with open(text_path_name,'w',encoding='utf-8') as fp:
        fp.write(text_content)
    pic_path_name = './qqKongJiangLibs/' + time +'.jpg'
    with open(pic_path_name,'wb') as fp:
        fp.write(pic_detail)
print("获取成功！！！")


sleep(10)
bro.quit()
