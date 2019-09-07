#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive
import os


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "rainsty020508182130"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument


    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = recMsg.Content
                    with open('./files/handle.txt', 'a') as f:
                        f.write('%s%s\n' % (toUser, content))
                    if content.strip() == "菜单":
                        content = "这是一个菜单\n输入1：查看历史消息\n输入2：查看历史图片"
                    elif content.strip() == "1":
                        content = os.popen("cat ./files/handle.txt | grep %s | tail -n 100 | awk -F '%s' '{print $2}'" % (toUser, toUser)).read()[:-1]
                    elif content.strip() == "2":
                        mediaId = os.popen("cat ./files/images.txt | grep %s | tail -n 1 | awk -F '%s' '{print $2}'" % (toUser, toUser)).read()[:-1]
                        if mediaId == "":
                            #mediaId = "ko6zjMTgHhXFSy2p8W4eupv9v6EVjidxvzta4rHcmaovSxVzREoDxa1MBl89Sotu"
                            mediaId = "1Plaf_sgdmVbg5Au_IzUfy_d20BvpQ05x0tSoJaBqtFH5aGB0eTyez6Uh48BSNNC"
                        replyMsg =  reply.ImageMsg(toUser, fromUser, mediaId)
                        return replyMsg.send()
                    elif content.strip() == "3":
                        content = "你真漂亮！"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    with open('./files/images.txt', 'a') as f:
                        f.write('%s%s\n' % (toUser, mediaId))
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print "暂且不处理"
                return reply.Msg().send()
        except Exception, Argment:
            return Argment

