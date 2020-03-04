import requests
import json


def get_url(url):
    try:
        headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/80.0.3987.122 Safari/537.36"}
        return requests.get(url, headers)
    except:
        raise TypeError('that\'s your fault!')


def my_close_name():
    #url = "https://y.qq.com/n/yqq/playlist/6547496770.html#stat=y_new.index.playlist.pic"
    url="https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=3&topid=6547496770&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010";
    content = get_url(url)
    #getcomment = re.findall('<ul>(.*?)</ul>',content);
    #print(content.text)
    aopen=json.loads(content.text);
    finallist=aopen['comment']['commentlist']
    a=0
    for openlist in finallist:
        a=a+1
        print("第%s条评论为:%s" %(a,openlist['rootcommentcontent']))
    #print(len(aopen['comment']['commentlist']))
    #(as)


if __name__ == '__main__':
    my_close_name()
