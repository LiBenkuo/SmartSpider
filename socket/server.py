#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket                        # import socket module

s = socket.socket()                  # create socket instance
host = socket.gethostname()          # get local host name
port = 8888                          # set port number
s.bind((host, port))                 # bind the port


s.listen(5)                          # wait for the client connect
while True:
  c, addr = s.accept()                 # create connect to the client 
  print 'connect addr: ', addr
  c.send('welcome! whoowa')
  c.close()                            # close the connect
