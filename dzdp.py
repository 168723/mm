import sys
import os
import re
import requests
import pymysql
from pyquery import PyQuery as pq
header_pinlun = {
'Host': 'www.dianping.com',
'Accept-Encoding': 'gzip',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36',
'Cookie':'navCtgScroll=0; _lxsdk_cuid=16cf0fdbf1561-0266f4c764b96b-6b111b7e-e1000-16cf0fdbf17c8; _lxsdk=16cf0fdbf1561-0266f4c764b96b-6b111b7e-e1000-16cf0fdbf17c8; _hc.v=b4da0ea5-9b43-609d-cb49-83838666b21c.1567411257; cye=hangzhou; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; ctu=5a917cdbd5b3a5f487d381238c2aa7fa2d12fe3851b903bdc1b9cdf8f3024ace; s_ViewType=10; td_cookie=2817421375; dper=9e7994ee21a6789be75fad35d7786bbfe003906c657c91a7910c647850f9d70a8402140b9432fd238a687542623669a7d8dee6de736f694432014e0ca5ba7a52c1b72cc8757261441604e040184593b2bac2905f727b20ac172687ac4e923af9; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_2124997298; _lxsdk_s=16ec5796a2c-630-113-5ba%7C1530432278%7C42',
}

header_css = {
'Host': 's3plus.meituan.net',
'Accept-Encoding': 'gzip',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'

}
def mysqlpy(shopName,shopAddress,shopPer,taste,environment,service):
    #连接数据库
    db = pymysql.connect("localhost","root","123456","dzdp_shop")
    # db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "INSERT INTO shopcontent_qz(shopName,shopAddress,shopPer,taste,environment,service) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(shopName,shopAddress,shopPer,taste,environment,service))  
    db.commit()  #提交数据
    cursor.close()
    db.close()

assessmentfont = TTFont('C:/Users/20233/Desktop/4b056322.woff')
assessment_TTGlyphs = assessmentfont['cmap'].tables[0].ttFont.getGlyphOrder()[2:]
assessment_dict = {}
for i, x in enumerate(assessment_TTGlyphs):
    assessment_dict[x] = i


tagfont = TTFont('C:/Users/20233/Desktop/0b355749.woff')
tag_TTGlyphs = tagfont['cmap'].tables[0].ttFont.getGlyphOrder()[2:]
tag_dict = {}
for i, x in enumerate(tag_TTGlyphs):
    tag_dict[x] = i    
    
    
# 导入下载好的字体    
addressfont = TTFont('C:/Users/20233/Desktop/9213d34e.woff')
address_TTGlyphs = addressfont['cmap'].tables[0].ttFont.getGlyphOrder()[2:]
address_dict = {}
for i, x in enumerate(address_TTGlyphs):
    address_dict[x] = i

    
perfont = TTFont('C:/Users/20233/Desktop/4b056322.woff')
per_TTGlyphs = perfont['cmap'].tables[0].ttFont.getGlyphOrder()[2:]
per_dict = {}
for i, x in enumerate(per_TTGlyphs):
    per_dict[x] = i

woff_string = '''
1234567890店中美家馆
小车大市公酒行国品发电金心业商司
超生装园场食有新限天面工服海华水
房饰城乐汽香部利子老艺花专东肉菜
学福饭人百餐茶务通味所山区门药银
农龙停尚安广鑫一容动南具源兴鲜记
时机烤文康信果阳理锅宝达地儿衣特
产西批坊州牛佳化五米修爱北养卖建
材三会鸡室红站德王光名丽油院堂烧
江社合星货型村自科快便日民营和活
童明器烟育宾精屋经居庄石顺林尔县
手厅销用好客火雅盛体旅之鞋辣作粉
包楼校鱼平彩上吧保永万物教吃设医
正造丰健点汤网庆技斯洗料配汇木缘
加麻联卫川泰色世方寓风幼羊烫来高
厂兰阿贝皮全女拉成云维贸道术运都
口博河瑞宏京际路祥青镇厨培力惠连
马鸿钢训影甲助窗布富牌头四多妆吉
苑沙恒隆春干饼氏里二管诚制售嘉长
轩杂副清计黄讯太鸭号街交与叉附近
层旁对巷栋环省桥湖段乡厦府铺内侧
元购前幢滨处向座下臬凤港开关景泉
塘放昌线湾政步宁解白田町溪十八古
双胜本单同九迎第台玉锦底后七斜期
武岭松角纪朝峰六振珠局岗洲横边济
井办汉代临弄团外塔杨铁浦字年岛陵
原梅进荣友虹央桂沿事津凯莲丁秀柳
集紫旗张谷的是不了很还个也这我就
在以可到错没去过感次要比觉看得说
常真们但最喜哈么别位能较境非为欢
然他挺着价那意种想出员两推做排实
分间甜度起满给热完格荐喝等其再几
只现朋候样直而买于般豆量选奶打每
评少算又因情找些份置适什蛋师气你
姐棒试总定啊足级整带虾如态且尝主
话强当更板知己无酸让入啦式笑赞片
酱差像提队走嫩才刚午接重串回晚微
周值费性桌拍跟块调糕'''

woffs = [i for i in woff_string if i != '\n' and i != ' ']

def woff_change(wofflist, TTG, woffdict):
    try:
        woff_content = ''
        for char in wofflist:
            text = str(char.encode('raw_unicode_escape').replace(b'\\u', b'uni'), 'utf-8')
            if text in TTG:
                content = woffs[woffdict[str(char.encode('raw_unicode_escape').replace(b'\\u', b'uni'), 'utf-8')]]
            else:
                content = char
            woff_content += ''.join(content)
    except UnicodeDecodeError:
        return "编码错误"
    else:
        return woff_content

#     soup为网页的内容
def get_adress(soup, address_TTGlyphs, address_dict):
    adress = soup("div.tag-addr > span").text()
    location = woff_change(adress, address_TTGlyphs, address_dict)
    locations=re.sub('\s','',location)
    return locations

def get_per(soup, per_TTGlyphs, per_dict):
    per = soup("div.comment > a.mean-price> b").text()
    shop_per = woff_change(per, per_TTGlyphs, per_dict)
    shop_pers=re.sub('\s','',shop_per)
    if(len(shop_pers)==0):
        shop_pers="暂无"
    return shop_pers


def get_tag(soup, tag_TTGlyphs, tag_dict):
    tag = soup("div.tag-addr> a > span.tag ").eq(0).text()
    shop_tag = woff_change(tag, tag_TTGlyphs, tag_dict)
    shop_tags=re.sub('\s','',shop_tag)
    return shop_tags



def get_assessment(soup, assessment_TTGlyphs, assessment_dict):
    assessment={}
    assessment[0] = soup("span.comment-list>span>b ").eq(0).text()
    assessment[1] = soup("span.comment-list>span>b ").eq(1).text()
    assessment[2] = soup("span.comment-list>span>b ").eq(2).text()
    shop_assessment={}
    shop_assessment[0] = woff_change(assessment[0], assessment_TTGlyphs, assessment_dict)
    shop_assessment[1] = woff_change(assessment[1], assessment_TTGlyphs, assessment_dict)
    shop_assessment[2] = woff_change(assessment[2], assessment_TTGlyphs, assessment_dict)
    shop_assessments={}
    shop_assessments[0]=re.sub('\s','',shop_assessment[0])
    shop_assessments[1]=re.sub('\s','',shop_assessment[1])
    shop_assessments[2]=re.sub('\s','',shop_assessment[2])
    if(len(shop_assessments[0])==0):
        shop_assessments[0]="暂无"
    if(len(shop_assessments[1])==0):
        shop_assessments[1]="暂无"
    if(len(shop_assessments[2])==0):
        shop_assessments[2]="暂无"

    return shop_assessments[0],shop_assessments[1],shop_assessments[2]


def content(url):
#     爬取页面
    html = requests.get(url,headers=header_pinlun)
    html.encoding='utf-8'
    print("1 ===> STATUS", html.status_code)
    doc = pq(html.text)
    shoplist = doc("div.shop-all-list > ul > li").items()
    for data in shoplist:
        shopName=data("h4").text()
        shopAddress=get_adress(data,address_TTGlyphs,address_dict)
        shopPer=get_per(data,per_TTGlyphs,per_dict)
        taste,environment,service=get_assessment(data,assessment_TTGlyphs,assessment_dict)
        print("~"*100)
        print("商铺名称：",shopName)
        print("店铺地址：",shopAddress)
        print("人均消费：",shopPer)
        print("效果",taste,"环境",environment,"服务",service)
        mysqlpy(shopName,shopAddress,shopPer,taste,environment,service)
    nexturl=doc("div.page > a.next").attr("href")
    if(nexturl==None):
        return 0
    else:
        content(nexturl)

url="http://www.dianping.com/search/keyword/3/50_%E9%BE%99%E6%B9%96%E6%9D%AD%E5%B7%9E%E9%87%91%E6%B2%99%E5%A4%A9%E8%A1%97"
content(url)
