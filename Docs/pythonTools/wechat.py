#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   wechat.py
@time:   2020-11-25 10:33:29
@description: windows登陆微信，执行脚本 python wechat.py XXX 13 20
"""

import sys
import datetime
import time
import win32clipboard
import win32con
import win32api
import win32gui
import random


WATER = """
人的一辈子有多少习惯，习惯用同一个杯子喝热水，时间长了以后改掉是一件很难得事情。
我只笑笑，拿起水杯喝水，手有点暖。寒冷的夜，除了我，还有热水暖你。
你知道喝酒跟喝水的分别吗？ 酒，越喝越糟糕 水，越喝越年轻。
喝水，喝的不是水，喝的是我对你深沉而又温暖的爱。
感情呀，像喝水。有人喜欢喝凉水，喜欢那种透彻心底的感觉。有人则喜欢喝温水，暖暖的。也有人喜欢喝热水，能带来火热的感觉，我希望你喝热水，因为它像我对你爱的感觉。
如果喝水能喝醉，那你要喝热水，醉倒我怀里会更暖。
喜欢你喝水的时候把吸管咬的扁扁的，喜欢你穿着球鞋在落叶上踩来踩去。
其实水和酒一样，只是水能解渴，酒能解愁，有时候酒并不能解愁，所以和酒还不如喝水，喝水更健康。
喝水时，若你先倒冷水，再倒热水，那你会越喝越寒；但是如果你是先倒热水再倒冷水，就会越喝越暖。
吃药时喜欢干吞不喝水，会有人拿来一杯水说着恐吓的话逼着你喝，这样就是所谓的幸福了吧！你就是那个吃药不喝水的女人，很庆幸，我会拿来一杯热水陪着你。
不知道何时以后，你喜欢上了喝水 ，因为我知道这是你爱我的习惯。
想喝水时，仿佛能喝下整个大海；
喝水也一样开心，所以你要多喝水才能活得比别人快乐。
一个人恋爱了，喝水像奶茶。
水是蔚蓝色的，没有风的时候水像一面明亮的大镜子，风一吹水库的水就泛起了一层一层的波纹。
捡起一块小石子投进小河里，顿时，激起了一层层涟漪，逐渐的扩大，扩大……水中的月亮也随着波纹破碎，一圈圈荡漾开来。
人若时常喝水，修得透明如水、心静如水，善莫大焉。
一家三口都醒了，吃奶的、喝水的、刷牙的，热热闹闹，各得其所. 这也是以后我向往的生活。
天上的云彩变化多端，有时像一匹骏马在奔驰，有时像一条狗在摆头摇尾，有时像一只鸡在找食，有时又像一头大象在喝水。
一只小羊在河边喝水，狼见到后，便想找一个名正言顺的借口吃掉他。于是他跑到上游，恶狠狠地说小羊把河水搅浑浊了，使他喝不到清水。
多喝水,清洗润滑你的身体。这也有助于你的皮肤保持湿润、光滑，富有青春活力。水是最有益于健康的饮料。
人生就像一张茶几，上面摆着各种杯具，浮生苦茶就在杯具中。生活中到处都是杯具，喝水的、装水的、超市卖的、冰箱冻着的。在这充满水的时间，我希望你钟爱热水，钟爱我。
宝宝该喝水咯，多喝水才身体棒棒哒！
你的大宝贝求你多喝水呦！
这是一条温馨的喝水提醒。
宝贝快看这里，有水杯哦！
你的小水杯正等着你去吻它哦！
喝了我的水，就是我的人了哦！
水生来就是要被你的肚肚温暖的哦！
我不贩卖水，我就是想让水成为你！
如果你爱我，就请喝掉我！(来自大宝贝的独家告白)
你是水，我是水，大家都是水，而你是我唯一的水水，吸溜吸溜！
""".split('\n')[1:-1]

MORNING = """
早安宝贝
宝宝早安
宝宝该起床啦，别睡觉啦，太阳照到PP啦！
""".split('\n')[1:-1]

NIGHT = """
宝宝回家没啊，都晚上七点了，辛苦了，爱你呦！
宝宝该睡觉咯，早点睡觉身体棒棒哒！
""".split('\n')[1:-1]


def move(x, y):
    win32api.SetCursorPos((x, y))


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def paste():
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(86, 0, 0, 0)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


def enter():
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


def paste_text(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()


def send_message():
    win32api.keybd_event(18, 0, 0, 0)
    win32api.keybd_event(83, 0, 0, 0)
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)


def main(_name, _text):
    hwnd = win32gui.FindWindow("WeChatMainWndForPC", None)
    time.sleep(1)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    time.sleep(1)
    win32gui.MoveWindow(hwnd, 0, 0, 600, 600, True)
    time.sleep(1)
    move(28, 148)
    click()
    time.sleep(1)
    move(148, 36)
    click()
    time.sleep(1)
    paste_text(_name)
    paste()
    time.sleep(1)
    enter()
    time.sleep(1)
    paste_text(_text)
    time.sleep(1)
    paste()
    send_message()
    time.sleep(1)
    win32gui.MoveWindow(hwnd, 0, 720, 600, 600, True)
    time.sleep(1)


if __name__ == "__main__":
    name = str(sys.argv[1])
    hour = int(sys.argv[2])
    minute = int(sys.argv[3])

    while True:
        now_time = datetime.datetime.now()

        if now_time.hour >= 7:
            if now_time.hour <= 22 and now_time.minute == minute:
                i = random.randint(0, len(WATER)-1)
                print(i)
                main(name, WATER[i])

        if now_time.hour == hour and now_time.minute == minute:
            main(name, MORNING[0])

        if now_time.hour == hour and now_time.minute == minute + 5:
            main(name, MORNING[1])

        if now_time.hour == hour and now_time.minute == minute + 15:
            main(name, MORNING[2])

        if now_time.hour == 19 and now_time.minute == 0:
            main(name, NIGHT[0])

        if now_time.hour == 23 and now_time.minute == 0:
            main(name, NIGHT[1])

        print(now_time)
        time.sleep(50)
