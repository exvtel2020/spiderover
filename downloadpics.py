#rtx id heliang01
import requests
from urllib import request
import time
import re
import pip
from lxml import etree
import os

def get_url(url):

    src_list = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'referer':'https: // www.douyu.com /',
        'cookie': 'dy_did=b6f2b56dab59405ee3f57c8900021501; acf_did=b6f2b56dab59405ee3f57c8900021501; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1584266829; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1584273469'
    }
    res = requests.get(url, headers = headers)
    patten = re.compile(r'(https://rpic.douyucdn.cn/asrpic/\d+/\d+_\d+.png)')
    src_list = re.findall(patten, res.text)
    print(src_list.__len__())
 #   print(src_list)
    down_list = set(src_list)
    print(down_list.__len__())
    print(down_list)
    i = 0
    file_dic = os.getcwd()+r'\pics\\'
    if not os.path.exists(file_dic):
        os.mkdir(file_dic)
    for down_url in down_list:

        file_name = re.findall(r'(\d+_\d+.png)',down_url)
        dicfile = os.path.exists(file_dic)
        try:
            if dicfile:
                request.urlretrieve(down_url, file_dic  + file_name[0] )
                time.sleep(2)
            else:
                os.makedirs(file_dic)
                request.urlretrieve(down_url,  file_dic + file_name[0] )
                time.sleep(2)
            print("下载文件 " + file_name[0] + " 成功！")
            i += 1
        except:
            print(down_url + " 下载失败")
    print("一共%s个文件下载完毕!"%i)
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def main():
#    url = "https://www.douyu.com/g_wzry"
    install("lxml")
    url = input("请输入要下载斗鱼网站的url地址：").strip()
    get_url(url)

if __name__ == "__main__":
    main()