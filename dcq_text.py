import requests
from lxml import etree
import json
import random
import string

def page_de(url):
    print("已进入学校要闻第{}网页！！！！".format(url))
    # print(url)
    respo = requests.get(url).content
    data = etree.HTML(respo)
    text_list = data.xpath('//div[@class="media"]/h4/a/text()')
    hreft_list = data.xpath('//div[@class="media"]/h4/a/@href')
    # print('text_list len',len(text_list))
    # print('hreft_list len',len(hreft_list))
    dic ={}
    for k,v in zip(text_list,hreft_list):
        dic[k] = v
    # print("======")
    # print(dic.keys())
    for i in list(dic.keys()):
        print(i)
        # wanp = input("请输入你需要的标题：")
    wanp = input("请输入你需要的标题：")
    if wanp=='':
        print("NEXT")
    else:

    # key_li = list(dic.keys())

        if str(wanp) in str(dic.keys()):

            # print(dic.keys())
            want_url = dic[str(wanp)]
            print("已检索到你所需要的链接：",want_url)
            wan_url = str(want_url)
            resp = requests.get(url=wan_url,verify=False).content
            data_w = etree.HTML(resp)
            # du = data_w.xpath('//div[@class="cuhksz-detail-content"]')
            du_title = data_w.xpath('//div[@class="cuhksz-detail-content"]/h1/text()')
            du_anther = data_w.xpath('//div[@class="cuhksz-detail-content"]/ul/li/text()')
            du_span = data_w.xpath('//div[@class="cuhksz-detail-content"]//p//span/text()')
            print(''.join(du_title))
            print(''.join(du_anther))
            print(''.join(du_span))
            with open('du_tea.txt','a') as f:
                print("开始下载文章标题！！！！")
                f.write(''.join(du_title) + '\n')
            with open('du_tea.txt','a') as f:
                print("开始下载文章作者！！！！")
                f.write(''.join(du_anther) + '\n')
            with open("du_tea.txt",'a') as f:
                print("开始下载文章内容！！！！")
                f.write(str(du_span) + '\n')
            print("文档保存完成！！！")
            #图片下载
            img_urls = data_w.xpath('//div[@class="cuhksz-detail-content"]//p//span/img/@src')
            img_title = data_w.xpath('//div[@class="cuhksz-detail-content"]//p//span/img/@title')
            # print(img_urls)
            # print(img_title)
            for i in range(len(img_urls)):
                # img_d = requests.get(url=img_url).content
                # img_data = etree.HTML(img_d)
                # img_name = random.randint(900,1000)
                # img_name_t = img_name + ".png"
                with open(img_title[i],'wb+') as f:
                    print("开始下载图片！！！！")
                    img_d = requests.get(url=img_urls[i]).content
                    f.write(img_d)
                    print("图片下载完成！！！！")


# want = input("请输入需要的标题：")
#校园要闻第一页
# print("已进入校园网站首页，开始检索学校要闻首页！！！")
url = 'https://www.qjnu.edu.cn/'
res = requests.get(url).text
ress = etree.HTML(res)
href_l = ress.xpath('//div[@class="cuhksz-news"]/div[@class="cuhksz-column-title"]/a/@href')

#学校要闻第一页url
xx_url = href_l[0]
print('已获取学校要闻首页链接：',format(xx_url))
#进入学校要闻第一页url
respo = requests.get(url=xx_url).content
data = etree.HTML(respo)
next_url_list = data.xpath('//ul[@class="pager"]/li/a/@href')
# print(next_url_list[1:])
for next_url in next_url_list[1:]:
    page_de(next_url)





