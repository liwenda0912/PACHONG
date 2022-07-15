from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor


def Read(m, dri):
    lists = []
    for url1 in m:
        dri.get(url=url1)
        page_html = dri.page_source
        t1 = etree.HTML(page_html)
        b = t1.xpath('//div[@class="main-content-wrap fl"]//div[@class="right-book-list"]/ul/li//div/h3/a/text()')
        for da in b:
            lists.append(da)

    print(lists)


def main():
    dri = webdriver.Chrome(executable_path='chromedriver')  # 打开浏览器
    dri.get("https://www.readnovel.com/all")

    dri.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    page_html = dri.page_source
    m = []
    t = etree.HTML(page_html)
    # 翻页并模拟点击

    with ThreadPoolExecutor(100) as t:
        for i in range(1, 4):
            urls = dri.current_url
            m.append(urls)
            dri.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            a = dri.find_element(By.CSS_SELECTOR, '#page-container > div > ul > li:nth-child(9) > a')
            a.click()
        t.submit(Read, m, dri)
    dri.close()  # 关闭浏览器
    dri.quit()  # 退出浏览器


if __name__ == '__main__':
    main()
