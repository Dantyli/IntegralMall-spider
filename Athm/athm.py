#encoding=utf-8
import json
from bs4 import BeautifulSoup as bs
from urllib.request import Request,urlopen
class Athm():
    def __init__(self):
        super(Athm,self).__init__()
        self.url='http://athmall.com/get_merchantsgoods_details.shtml?id={0}'
        self.dict={}
    def readHtml(self,html):
        req=Request(html)
        resp=urlopen(req)
        content=resp.read() 
        charset=resp.headers.get_content_charset()
        content=content.decode(charset)
        return content
    def getPrice(self):
        for id in range(10000,10010):#商品id 10000-10010 的商品
            link=self.url.format(id)
            body=self.readHtml(link)
            soup=bs(body,'html.parser')
            price=soup.find_all('span',class_='goodsmap_pay_maney')[0].string
            inte=soup.find_all('span',class_='goodsmap_pay_integer')[0].string
            total_price=float(price)+float(inte)
            name=soup.find_all('span',class_='search_key')[1].string
            self.dict[name]=total_price #储存数据
        dic=self.dict
        js=json.dumps(dic,ensure_ascii=False)
        filename='download.json'
        with open(filename,'w',encoding='utf-8') as f:
            f.write(js)
            print('下载完成')
if __name__=='__main__':
    a=Athm()
    a.getPrice()
