import requests
from lxml import etree
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
        'host': 'www.qjnu.edu.cn',

        }
page_url = 'https://www.qjnu.edu.cn/contents/9260/154880.html'
response = requests.get(url=page_url, headers=headers, verify=False).content
page_data = etree.HTML(response)
data_list = page_data.xpath('//div[@class="cuhksz-detail-content"][1]')
for data in data_list:
    page_title = data.xpath('//div[@class="cuhksz-detail-content"][1]/h1/text()')
    page_time = data.xpath('//div[@class="cuhksz-detail-content"][1]/ul/li[1]/text()')
    page_sou = data.xpath('//div[@class="cuhksz-detail-content"][1]/ul/li[2]/text()')
    page_text = data.xpath('//div[@class="cuhksz-detail-content"][1]/div[@class="cuhksz-detail-word"]//p/span/text()')
    # 判断是否有图片
    try:
        page_img = data.xpath('./div[@class="cuhksz-detail-word"]//p/span/img/@src')
        # 实例链接 https://www.qjnu.edu.cn/upload/images/2022/5/5ddf09a39d979ded.jpg
        print('图片链接是', page_img)
    except:
        print('此网页没有图片！！！')
        break
print(page_title, page_time, page_sou, page_text)