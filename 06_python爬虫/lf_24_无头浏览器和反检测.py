from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver import EdgeOptions
from time import sleep

# 实现无可视化的操作
edge_options = Options()
edge_options.add_argument('--headless')
edge_options.add_argument('--disable-gpu')

# 如何实现selenium不被检测到的风险
option = EdgeOptions()
option.add_experimental_option('excludeSwitches',['enable-automatioan'])
# 无可视化界面
bro = webdriver.Edge(executable_path='./msedgedriver.exe',options=option)
bro.get('https://www.baidu.com')
page_text = bro.page_source
print(page_text)
sleep(2)
bro.quit()