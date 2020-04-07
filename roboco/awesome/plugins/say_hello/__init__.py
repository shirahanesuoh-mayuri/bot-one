from nonebot import on_command,CommandSession
from nonebot import get_bot

bot = get_bot()
@on_command("hello",only_to_me=False,aliases=("早安"))
async def hello(session:CommandSession):
    await session.send("呐讷，米娜桑，哦哈哟")
