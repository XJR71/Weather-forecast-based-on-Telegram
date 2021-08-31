import requests
import json

key = '825154fad3f9efda549cfb5ef1404391'
def geo(address:str)->dict:
    parameters1 = {'key':key,'address':address}
    res1 = requests.get("https://restapi.amap.com/v3/geocode/geo?parameters",params=parameters1)
    jd1 = json.loads(res1.text)
    coord1 = jd1['geocodes'][0]['location']
    return coord1

def routeB(url:str,origin:str,destination:str)->dict:
    paramatersB = {'key': key, 'origin': origin, 'destination': destination}
    resB = requests.get(url, paramatersB)
    jdB = json.loads(resB.text)
    coordB = jdB['route']['taxi_cost']['steps']
    print(coordB)
"""
def route1(origin:str,destination:str)->dict:
    parameters = {'key':key,'origin':origin,'destination':destination}
    res2 = requests.get("https://restapi.amap.com/v3/direction/walking?parameters",params=parameters)
    jd2 = json.loads(res2.text)
    print(jd2)
    coord2 = jd2['route']['paths'][0]['steps']
    print(coord2)
    len_1=len(coord2)
    #a = str('路径为'+str(len_1)+'步')
    #print(a)
    for i in range (0,len_1):
        b = coord2[int(i)]['instruction']
        print(b)
    #return coord1
"""



def routeW(url:str,origin:str,destination:str)->dict:
    paramatersB = {'key': key, 'origin': origin, 'destination': destination}
    resB = requests.get(url, paramatersB)
    jdB = json.loads(resB.text)
    print(jdB)
    #coordB = jdB['route'][0]['paths'][0]['steps']
    #print(coordB)




def routeD(origin:str,destination:str)->dict:
    paramaters = {'key':key,'origin':origin,'destination':destination}
    res2 = requests.get(url,params=paramaters)
    jd2 = json.loads(res2.text)
    print(jd2)

    coord2 = jd2['route'][0]['paths'][0]
    print(coord2)



def routeR(url: str, origin: str, destination: str) -> dict:
    paramaters = {'key': key, 'origin': origin, 'destination': destination}
    res2 = requests.get(url, paramaters)
    jd2 = json.loads(res2.text)
    coord2 = jd2['data']['paths'][0]['steps']
    print(coord2)



def greetingd():
    print('您好，我是您的出行小助手，有什么能够帮您的吗？')


greetingd()

message = input()
if message=='路线规划':
    print("请问您想使用什么交通工具呢？")
    ideal_transport=input()
    if ideal_transport=='步行' or '走路':
        url = 'https://restapi.amap.com/v3/direction/walking?parameters'
        start = geo(input("请问您的出发地点是？"))
        end = geo(input("请问您的目的地是？"))
        routeW(url,start,end)

    elif ideal_transport=='骑自行车' or '骑车':
        url = 'https://restapi.amap.com/v4/direction/bicycling?parameters'
        start = geo(input("请问您的出发地点是？"))
        end = geo(input("请问您的目的地是？"))
        routeR(url,start,end)

    elif ideal_transport=='坐公交' or '公交' or '公交车':
        url = 'https://restapi.amap.com/v3/direction/transit/integrated?parameters'
        start = geo(input("请问您的出发地点是？"))
        end = geo(input("请问您的目的地是？"))
        routeB(url,start,end)
    elif ideal_transport == '开车' or '驾车':
        url = 'https://restapi.amap.com/v3/direction/driving?parameters'
        start = geo(input("请问您的出发地点是？"))
        end = geo(input("请问您的目的地是？"))
        routeD(url,start,end)
