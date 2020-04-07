from nonebot import on_command,CommandSession
from nonebot import get_bot
import urllib.request
from bs4 import BeautifulSoup
import requests
import re
from time import sleep
from selenium import webdriver
import os

bot = get_bot()
@on_command("pic_search",only_to_me=False,aliases=("图片搜索"))
async def pic_serach(session:CommandSession):
    city = session.get('city', prompt='你想查询哪个图片呢？')
    get_url(city)
    await session.send("糙汉子翻找中")
    imginfo = get_img_info()
    if imginfo == 'error':
        await session.send("没找到啊....")
    else:
        await session.send("找到了\n图片名:"+imginfo[0]+"\n"+imginfo[1]+imginfo[2]+"\n画师："+imginfo[3])
def get_url(city):
    reg = 'url=(.+?\?term=2)'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, city)
    imgurl = imglist[0]
    response = requests.get(imgurl)
    img = response.content
    path = 'F:/CQA-tuling/roboco/awesome/plugins/pic_search/a.jpg' 
    with open (path,'wb') as f:
        f.write(img)
def get_img_info():
    url = 'https://saucenao.com/index.php'
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    dr = webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver",chrome_options=option)
    dr.get(url)
    dr.implicitly_wait(10)
    print(dr.find_element_by_xpath('/html/head/title'))
    dr.find_element_by_id('file').send_keys('F:/CQA-tuling/roboco/awesome/plugins/pic_search/a.jpg')
    dr.find_element_by_xpath('//*[@id="Search"]/form/input[2]').click()
    sleep(10)
    print(dr.find_element_by_xpath('/html/head/title'))
    html = dr.execute_script("return document.documentElement.outerHTML")
    htmlinfo = html
    soup = BeautifulSoup(htmlinfo,'lxml')
    contentname = soup.select('#middle > div:nth-child(2) > table > tbody > tr > td.resulttablecontent > div.resultcontent > div.resulttitle > strong')
    contentid = soup.select('#middle > div:nth-child(2) > table > tbody > tr > td.resulttablecontent > div.resultcontent > div.resultcontentcolumn > strong:nth-child(1)')
    contentidnum = soup.select('#middle > div:nth-child(2) > table > tbody > tr > td.resulttablecontent > div.resultcontent > div.resultcontentcolumn > a:nth-child(2)')
    contentmemid  = soup.select('#middle > div:nth-child(2) > table > tbody > tr > td.resulttablecontent > div.resultcontent > div.resultcontentcolumn > a:nth-child(6)')
    if len(contentname)==0 or len(contentid)==0 or len(contentmemid)==0 or len(contentidnum)==0:
        return 'error'
    else:
        infolist = [contentname[0].get_text(),contentid[0].get_text(),contentidnum[0].get_text(),contentmemid[0].get_text()]
        return infolist
    
    #path = 'F:/CQA-tuling/roboco/awesome/plugins/pic_search/a.jpg'  
    #if os.path.exists(path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        #os.remove(path)  
    #return content1,content2,content3
    
    

    
