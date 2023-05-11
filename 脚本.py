import requests
import datetime
import yagmail
import time as Time
import pymysql


startTime, endTime = "08:00", "21:30"
time = datetime.datetime.now().strftime("%Y-%m-%d")
yag = yagmail.SMTP(
    user="2807704365@qq.com", password="nxnplpsplhnedcfh", host="smtp.qq.com"
)
db = pymysql.connect(host='localhost',
                     user='test1',
                     password='123456',
                     database='test1',
                     charset='utf8')
cursor = db.cursor()
cursor.execute('select * from users where flag = 1')
users = list(cursor.fetchall())
sessions = [requests.session() for i in range(len(users))]
flags = [0] * len(users)
id = 0

data = {
    "commit": "Sign in",
    "uname": "",
    "password": "",
    "webauthn - support": "supported",
    "webauthn - iuvpaa - support": "unsupported",
}


def login():
    session = sessions[id]
    session.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    url = "https://passport2.chaoxing.com/fanyalogin"
    session.post(url=url, data=data)


def signin(user):
    session = sessions[id]
    url = (
        "https://office.chaoxing.com/front/third/apps/seatengine/code?id=" +
        user[2] + "+&seatNum="
        + user[3]
        + "&seatId=796"
    )
    token = ""
    res = session.get(url).text
    if "token: '" not in res:
        print("uname = {}: Not Found token".format(user[0]))
        print(res)
        return
    i = res.index("token: '") + 8
    while res[i] != "'":
        token += res[i]
        i += 1
    url = "https://office.chaoxing.com/data/apps/seatengine/submit?roomId="+user[2]+"&captcha=&startTime=" + startTime + \
        "&endTime=" + endTime + "&day=" + time + "&captcha=&seatNum=" + \
        user[3] + "&token=" + token + "&type=1"
    r = session.get(url).text
    print(user[0],"的签到结果: ",r)
    if len(r) > 300:
        flags[id] = 1


def cancel():
    session = sessions[id]
    url = "https://office.chaoxing.com/data/apps/seatengine/reservelist?cpage=1&pageSize=1&type=-1&seatId=796"
    res = session.get(url).json()
    canceId = res["data"]["reserveList"][0]["id"]
    url = "https://office.chaoxing.com/data/apps/seatengine/cancel?id=" + \
        str(canceId)
    res = session.get(url).text


def sendemail(user):
    news = requests.get(url="https://v1.hitokoto.cn?c=d&c=j&c=k").json()["hitokoto"]
    room = {'1900':"五楼西-电子预览室",'1901':"五楼东-自习室"}
    contents=[
        "教室: " + room[user[2]],
        "座位: " + user[3],
        "每日一言： " + news
        ]
    yag.send(user[4], "抢座成功", contents)


def cycle():
    for i in range(3):
        global id
        id,stage = 0,['登录','签到','发邮件']
        for user in users:
            try:
                data["uname"],data["password"] = user[0],user[1]
                if i == 0:
                    login()
                elif i == 1:
                    if datetime.datetime.now().hour >= 8:
                        cancel()
                    else:
                        p = 1
                        while datetime.datetime.now().minute < 45:
                            p = 0
                        if p == 0:
                            Time.sleep(1.5)
                    signin(user)
                    print('-' * 100)
                else:
                    if flags[id] and datetime.datetime.now().hour < 8:
                        sendemail(user)
            except Exception:
                print(user[0],'在{}阶段出现异常'.format(stage[i]))
                print(Exception)
                pass  
            id += 1


if __name__ == "__main__":
    cycle()