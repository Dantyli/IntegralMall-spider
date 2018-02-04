#ecoding=utf-8
import requests
import json
import time
#格式化当前日期
noTime=time.localtime(time.time())
nowTime=time.strftime('%y-%m-%d',noTime)
def flightInfo():
    url='http://athmall.com/getPlaneList_wap.shtml'
    allinfo=[]
    param={
        'time':nowTime,
        'start_code':'SZX',
        'arrive_code':'BJS',
        'price_high_low':'0',
        'time_long_short':'',
        'psgtype':'1'
    }
    r=requests.get(url,params=param)
    req=r.json()
    reql=req['list']#航班信息
    for n in range(1,len(reql)):
        info={}
        flightName=reql[n]['FlightNo']
        flightNo=reql[n]['MinFare']
        offTime=reql[n]['OffTime']
        count=reql[n]['MinDiscount']
        info[flightName]=flightNo
        info['起飞时间']=offTime
        info['余票']=count
        allinfo.append(info)
    print(allinfo)
flightInfo()