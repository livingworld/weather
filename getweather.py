import json
import sys
import requests
import time

history_weather_list=[]#历史天气查询记录list
def dumpTianqi(result):
    #最后进行解析
    dic = result
    weatherlist=[]#将读取的天气信息装进list内
    weatherlist.append(['城市:',dic["results"][0]["location"]["name"]])#读取返回的result中的字典内容，进行输出
    weatherlist.append(['天气:',dic["results"][0]["now"]["text"]])
    weatherlist.append(['温度:',dic["results"][0]["now"]["temperature"]+'℃'])
    weatherlist.append(['数据更新时间:',dic["results"][0]["last_update"]])
    weatherlist.append(['查询天气的时间 :',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
    #函数time.time()用于获取当前时间戳
    weatherstring=''#将list内的查询的天气内容转化为字符串的形式，使返回的内容为字符串形式，方便控件调用。
    for item1 in weatherlist:
            weatherstring=weatherstring+''.join(item1)+'   '
            #weatherstring=weatherstring+item1[0]+item1[1]+'  '#通过这一步可以实现
    #weatherstring1=weatherstring+'\n'#查询记录换行，方便历史查询
    history_weather_list.append(weatherstring)#每次查询的记录保存在历史天气查询list当中
    return(weatherstring)#返回天气查询的记录

'''result = requests.get(url, params, timeout)，发送get请求'''
def fetchWeather(location):
    API = 'https://api.thinkpage.cn/v3/weather/now.json'
    KEY='xl42ljwdjatghvnw'
    LANGUAGE='zh-Hans'
    UNIT='c'
#通过 parse 将请求参数转为字符串
    result = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    })
    result = result.text
    result = json.loads(result)
    return result

def history_weather():
    history_weather_info=history_weather_list
    #for item2 in history_weather_list:
    #    history_weather_info='\n'.join(history_weather_list)
    return history_weather_info#以字符串形式返回历史查询记录

def help_weather():
    return '''输入城市名或拼音，点击"查询按钮获取该城市的天气情况；
            点击"帮助"按钮,获取帮助文档；
            点击"历史"查询按钮,获取查询历史；
            点击"离开"，退出天气查询系统。'''

def quit_weather():
    return quit()
