import os
import telebot
import requests
import json
import spacy


nlp = spacy.load("zh_core_web_md")

#gaode API
key = '5fce40d90672d47abfe66d24c731ec32'

# API_KEY = os.getenv('1949831023:AAFnOBN6PLOSP5gG3zyhhq2nfAKxVKsMxjU')
bot = telebot.TeleBot('1949831023:AAFnOBN6PLOSP5gG3zyhhq2nfAKxVKsMxjU')
#设置代理

proxies={
'http':'127.0.0.1:7890',
'https':'127.0.0.1:7890',
'ssl':'127.0.0.1:7890'
}

"""
def ask_weather(city: str):
  parameters3 = {'key': key, 'city': city}
  res3 = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?parameters', parameters3,proxies=proxies)
  jd3 = json.loads(res3.text)
  coord3 = jd3['lives'][0]['weather']
  coord4 = jd3['lives'][0]['humidity']
  str_wea = ('你好，你所查询的城市当前天气为' + coord3 + ',湿度为' + coord4)
  return str_wea
"""

def affirm_date(message):#确定查询日期
  doc = nlp(message.text)
  affirmed_date =''
  for ent in doc.ents:
    if ent.label_=="DATE":
      affirmed_date = ent.text
      return affirmed_date
    else: continue
  return affirmed_date


def affirm_location(message):#确定查询地点
  doc = nlp(message.text)
  affirmed_location = ''
  for ent in doc.ents:
    if ent.label_=="GPE":
      affirmed_location = ent.text
      return affirmed_location
    else: continue
  return affirmed_location
"""

def affirmed_all(message):#再次确认
  if affirm_location(message):
    bot.send_message(message.chat.id,"请问您想查询什么地方的天气呢？")
    affirm_location(message)
  if affirm_date(message):
    bot.send_message(message.chat.id,"请问您想查询哪一天的天气呢？")
    affirm_date(message)
  else:
"""




@bot.message_handler(commands=['你好'])
def ask_weather(message):
  bot.reply_to(message,"请问有什么可以帮助您的吗？")



#@bot.message_handler(commands=['hello'])
#def hello(message):
  #bot.send_message(message.chat.id,weather)



def weather_forecast(message):#确定是否包含具体地点
  doc = nlp(message.text)
  for ent in doc.ents:
    if ent.label_=='GPE':
        return True
    else:
        return False



@bot.message_handler(func=weather_forecast)
def send_forecast(message):
  date = affirm_date(message)
  if date =='今天':
    extensions = 'base'
  else: extensions = 'all'
  request = affirm_location(message)
  #request = message.text.strip('/')
  parameters ={'key': key, 'city': request,'extensions':extensions}
  res3 = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?parameters', parameters,proxies=proxies)
  data = json.loads(res3.text)
  print(data)
  if date=='今天':
    bot.send_message(message.chat.id,'您要查询的城市天气为'+data['lives'][0]['weather']+'温度为'+data['lives'][0]['temperature'])
  elif date == '明天':
    bot.send_message(message.chat.id,'您要查询的城市天气为' + data['forecasts'][0]['casts'][1]['dayweather'] + '温度为' + data['forecasts'][0]['casts'][1]['daytemp']+'度')
  elif date == '后天':
    bot.send_message(message.chat.id, '您要查询的城市天气为' + data['forecasts'][0]['casts'][2]['dayweather'] + '温度为' +data['forecasts'][0]['casts'][2]['daytemp']+'度')


bot.polling()
