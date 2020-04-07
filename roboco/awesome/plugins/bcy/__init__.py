
from nonebot import on_command,CommandSession
from nonebot import get_bot
import random

bot = get_bot()
@on_command("bcy",only_to_me=False,aliases=("二次元语录"))
async def bcy(session:CommandSession):
    await session.send ("糙汉子思考中")
    fd = open( r'F:/CQA-tuling/roboco/awesome/plugins/bcy/yuliao.txt', "r" ,encoding="utf-8") 
    result=list(fd)
    fd.close()
    print (len(result))
    b=len(result)-1
    a = random.randint(0,b)
    print (a)
    
    await session.send(result[a])


