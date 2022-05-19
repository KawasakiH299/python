import requests
from lxml import etree
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
from time import sleep
import gevent
import queue
use_in = input("请输入关键词：")
url_0 = "https://www.qjnu.edu.cn/channels/9260.html"
# next_queue = queue.Queue()
def start(url,use_in,que_n):
    response = requests.get(url=url, headers=headers, verify=False).content
    use_data = etree.HTML(response)
    title = use_data.xpath('//div[@class="tab-pane active cuhksz-news-list fadein"]/div/h4/a/text()')
    address = use_data.xpath('//div[@class="tab-pane active cuhksz-news-list fadein"]/div/h4/a/@href')
    print("len(title)是{}，len(address)是{}".format(len(title),len(title)))
    print(use_in)
    for i in range(len(address)):
        if use_in in title[i]:
            print(title[i])
            print(address[i])
            que_n.put(address[i])
            job_two = gevent.spawn(next_p,address[i])
    print("暂停1秒")
    sleep(1)

def next_p(url):
    respons = requests.get(url=url, headers=headers, verify=False).content
    use_dat = etree.HTML(respons)
    print(use_dat.xpath('//text()'))

    data_list = use_dat.xpath('//div[@class="cuhksz-detail-content"][1]')
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
job_list = []
next_queue = queue.Queue()
for i in range(50):
    url = url_0[:-5] + '_' + str(i) + '.html'
    job = gevent.spawn(start, url,use_in,next_queue)
    job_list.append(job)
gevent.joinall(job_list)
