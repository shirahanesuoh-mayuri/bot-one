from nonebot import on_command,CommandSession
from nonebot import get_bot

bot = get_bot()
@on_command("help",only_to_me=False,aliases=("help","你能干嘛"))
async def hello(session:CommandSession):
    await session.send("呐，人家绝对服从尼酱的命令\n/早安，人家就能给尼酱问好\n/晚安，人家既可以和尼酱睡在一起\n/嘴臭，人家就会骂人(此功能容易招致群友的厌恶，请谨慎使用)\n/涩图，人家就会帮尼酱找来手O的图片\n\
/二次元语录，人家会战斗力爆棚！\n/运势，人家会为尼酱占卜nanodesu\n/每日一句，人家就会给你灌鸡汤\n/图片搜索，人家就能帮你找到你手O图片的来处哦")