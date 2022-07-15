import time
import pandas as pd
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By

lists = []
dri = webdriver.Chrome(executable_path='chromedriver')  # 打开浏览器
dri.get("https://www.taobao.com")
dri.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(5)
page_html = dri.page_source

t = etree.HTML(page_html)
# 翻页并模拟点击
a = dri.find_elements()
b = t.xpath('//div/div[@class="tb-recommend-content-item"]/a/div[@class="info-wrapper"]/div[@class="title"]/text()')
b.click()
for i in b:
    lists.append(i)
    d = pd.DataFrame(b)
    d.to_excel('data.xlsx', index=False)
# 保存writer中的数据至excel
# 如果省略该语句，则数据不会写入到上边创建的excel文件中

dri.close()  # 关闭浏览器
dri.quit()  # 退出浏览器
