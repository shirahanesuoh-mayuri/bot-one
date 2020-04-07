from datetime import datetime
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


'''
@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id='219524398',
                                 message=f'现在{now.hour}点整啦！,记得收菜')
    except CQHttpError:
        pass
'''
@nonebot.scheduler.scheduled_job('cron', hour = '4',minute = '0' )
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id='219524398',message='收菜收菜！@全体成员')
    except CQHttpError:
        pass
@nonebot.scheduler.scheduled_job('cron', hour = '8',minute = '30' )
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id='219524398',message='呐讷，米娜桑，哦哈哟,今天也要元气满满哦！kira~')
    except CQHttpError:
        pass
@nonebot.scheduler.scheduled_job('cron', hour = '23',minute = '30' )
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id='219524398',message='呐讷，米娜桑，哦呀斯密,晚上好梦哦！rua~')
    except CQHttpError:
        pass
