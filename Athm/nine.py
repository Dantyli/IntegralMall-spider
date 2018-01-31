#encoding:utf-8
import requests
import json
import matplotlib.pyplot as plt
def getNine():
    url='http://athmall.com/getNinePictures.shtml'
    r=requests.get(url,params={'num':0})
    req=r.json()
    reql=int(req[0]['count']/20)
    store_arr=[]
    for num in range(reql):
        nums={'num':num}
        r=requests.get(url,params=nums)
        req=r.json()
        reqf=req[1]
        for st in range(len(reqf)):
            if reqf[st]['storename'] not in store_arr:
                store_arr.append(reqf[st]['storename'])
            
    print(store_arr)
getNine()
        
