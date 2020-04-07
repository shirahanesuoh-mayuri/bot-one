from nonebot import on_command,CommandSession
from nonebot import get_bot
import random

bot = get_bot()
@on_command("lucky",only_to_me=False,aliases=("运势"))
async def lucky(session:CommandSession):
    await session.send("糙汉子祈祷中")
    luck = random.randint(0,1000)
    if luck>=800:
        await session.send("大吉")
    elif luck>=400 and luck < 800:
        await session.send("中吉")
    elif luck<400 and luck >= 200:
        await session.send ("末吉")
    else:
        await session.send("凶")

