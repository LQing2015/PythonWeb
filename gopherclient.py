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

s.sendall(filename+"\r\n")#向服务器发送请求！！

while 1:
	buf=s.recv(2048)#接受内容
	if not len(buf):
		break
	sys.stdout.write(buf)#输出到stdout
