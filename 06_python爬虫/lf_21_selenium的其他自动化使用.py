from selenium import webdriver
from time import sleep

bro = webdriver.Edge(executable_path='./msedgedriver.exe')
url = 'https://www.taobao.com/'
bro.get(url)
# 标签定位
search_input = bro.find_element_by_id('q')
# 标签交互
search_input.send_keys('Iphone')
# 滚轮滚动--执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)

# 点击搜索按键
btn = bro.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
btn.click()
sleep(2)
# 进行其他url请求
bro.get('https://www.baidu.com/')
# baidu_page_text = bro.page_source
# with open('./baidutest.html','w',encoding='utf-8') as fp:
#     fp.write(baidu_page_text)
sleep(2)
# 回退
bro.back()
taobao_page_text = bro.page_source
with open('./taobaotest.html','w',encoding='utf-8') as fp:
    fp.write(taobao_page_text)
sleep(5)
# 前进
bro.forward()
sleep(5)
bro.quit()
