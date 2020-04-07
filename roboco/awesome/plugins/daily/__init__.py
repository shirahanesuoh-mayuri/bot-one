from nonebot import on_command,CommandSession
from nonebot import get_bot

bot = get_bot()

import  requests
@on_command('daily',only_to_me=False, aliases=('每日一句',))
async def daily(session: CommandSession):
    daily_send = await get_daily()
    await session.send(daily_send[0])
    await session.send(daily_send[1])


async def get_daily():
    daily_sentence = get_content()
    return daily_sentence

def get_content():
    url = 'http://open.iciba.com/dsapi/'
    res = requests.get(url)
    content_e = res.json()['content']
    content_c = res.json()['note']
    return [content_c, content_e]
