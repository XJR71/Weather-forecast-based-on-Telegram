import requests
import json
key = '5fce40d90672d47abfe66d24c731ec32'
def ask_weather(city:str)->dict:
    parameters3 = {'key':key,'city':city}
    res3 = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?parameters',parameters3)
    jd3 = json.loads(res3.text)
    coord3 = jd3['lives'][0]['weather']
    coord4 = jd3['lives'][0]['humidity']
    print('你好，你所查询的城市'+asked_city+'当前天气为'+coord3+',湿度为'+coord4)
    print(coord3)
while 1:
    asked_city = input('请输入你要查询的城市:\n')
    ask_weather(asked_city)