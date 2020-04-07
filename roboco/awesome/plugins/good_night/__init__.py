from nonebot import on_command,CommandSession
from nonebot import get_bot
import emoji

bot = get_bot()
@on_command("goodnight",only_to_me=False,aliases=("晚安"))
async def goodnight(session:CommandSession):
    await session.send("呐讷，米娜桑，哦呀斯密")
    await session.send(emoji.emojize(':trophy:'))
