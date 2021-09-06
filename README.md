# Weather-forecast-based-on-Telegram
## Weather_forecast and Navigation Robot
### Here is the introduction about the Robot:  
The robot is called Sara. She is a robot or you can call her your assitant and it can help you search for some information about latest weather forecast or path planning.  
Just by telling her what you want to know and it will find some detailed information for you.  

Accessible information includes:  
Weather forecast：province，weather，temperature，winddirection，windpower，humidity，reporttime，nighttemp，nightweather.etc
Nvigation: Geocoding, inverse geocoding, origin, destination, paths, distance, duration, steps.etc

## Usage
### Find Sara  
Search "Sara" in Telegram and then you will find her in the list.  
![Find Sara](https://github.com/XJR71/Weather-forecast-based-on-Telegram/blob/master/photos/1.png)

### Starting Chat  
Click start or text "你好！" to start chatting with Sara.  
Now you can chat with her!  
![Greeting](https://github.com/XJR71/Weather-forecast-based-on-Telegram/blob/master/photos/2.png)
![Greeting](https://github.com/XJR71/Weather-forecast-based-on-Telegram/blob/master/photos/test1.gif)

### Ask questions or give her a task  
All you need to do is to send a message about what you kind of information you want to get:  
![Weather Forecast](https://github.com/XJR71/Weather-forecast-based-on-Telegram/blob/master/photos/test2.gif)  
Just give her a date and she will find the latest report for you!  
![Weather Forecast 2](https://github.com/XJR71/Weather-forecast-based-on-Telegram/blob/master/photos/test3.gif)  
![Weather Forecast 3](https://github.com/XJR71/Weather-forecast-based-on-Telegram/blob/master/photos/test4.gif)  

## Navigation Part  
In the navigation part, all you need to do is to give your place of departure and your destination, then she will ask you about the transportation you prefer. After you give a command like "on foot", she will find the closest way and show it to you.  
![Navigation](https://github.com/XJR71/Weather-forecast-based-on-Telegram/blob/master/photos/test5.gif) 
![Navigation](https://github.com/XJR71/Weather-forecast-based-on-Telegram/blob/master/photos/test6.gif) 

## Get more information  
If you want to get more infomation, you can visit GAODE API website to customise your own robot with your customised mission.  
![Information](https://github.com/XJR71/Weather-forecast-based-on-Telegram/blob/master/photos/111.png)  

## About Robot  

Using Telegram Python and Spacy 
Using GaoDe API to get weather data and geo data
Using zh_core_web_md to test Chinese
33766.MP4 is the 3X Video to show the function of the app
gaode api.py is the navigation part  
To get more information, you can visit:  
Python-Telegram-Bot-API: https://python-telegram-bot.readthedocs.io/en/stable/  
GAODE API: https://lbs.amap.com/api/webservice/summary
