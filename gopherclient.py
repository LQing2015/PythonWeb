#!/usr/bin/env python
#coding=utf-8
#利用套接字实现的Gopher协议！？？？是一个古老的信息查找系统？？？
#程序实现从主机上请求相关文档

import socket,sys

port=70#与web服务类似，但是它使用的是70
host=sys.argv[1]#这里可以填入一个地址guux.org
filename=sys.argv[2]#我们要请求的文件

#下面两行创建一个TCP连接S！！！
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

fd=s.makefile('rw',0)#这个函数把s变成了一个类似文本流一样的东西

fd.write(filename+"\r\n")

for line in fd.readlines():
	sys.stdout.write(line)
