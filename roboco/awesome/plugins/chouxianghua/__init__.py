from nonebot import on_command,CommandSession
from nonebot import get_bot
import requests
from bs4 import BeautifulSoup

bot = get_bot()
@on_command("zuichou",only_to_me=False,aliases=("嘴臭","嘴甜"))
async def zuichou(session:CommandSession):
    await session.send("糙汉子蓄力中")
    msg = session.ctx['message'][0]['data']['text']
    print(msg)
    if msg == '/嘴甜':
        await session.send(sentence())
    if msg == '/嘴臭':
        await session.send("target down，over")
        await bot.send_private_msg(user_id=session.ctx['user_id'],message = echou())
def sentence():
    url='https://s.nmsl8.club/loveword?type=1'
    response = requests.get(url)
    #response.encoding = response.apparent_encoding

    html = BeautifulSoup(response.text,'lxml')

    content = html.select('#words')

    return content[0].get_text()
def echou():
    url = 'https://s.nmsl8.club/loveword?type=2'
    response = requests.get(url)
    #response.encoding = response.apparent_encoding

    html = BeautifulSoup(response.text,'lxml')

    content = html.select('#words')

    return content[0].get_text()
