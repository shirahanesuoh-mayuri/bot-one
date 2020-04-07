from nonebot import on_command,CommandSession
from nonebot import get_bot
import urllib.request
from bs4 import BeautifulSoup
import requests
import re
import time
import requests
import re
from time import sleep
from selenium import webdriver
import os

bot = get_bot()
@on_command("setu",only_to_me=False,aliases=("涩图"))
async def setu(session:CommandSession):
    await session.send("涩图蓄力中.....")
    imgurl = getimg()+['error']
    while imgurl[0]=="error":
        getimg()
        imgurl =  getimg()+['error']
    string = imgurl[0]
    await session.send ("涩图爆发！")
    await session.send(string)
def getimg():
    html = getHtml("http://yunjie.f06.87yun.club/st")
    reg ='src="(.+?\.jpg)"'        #正则表达式
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html.decode('utf-8'))
    return imglist
def getHtml(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html






