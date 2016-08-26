#!/usr/bin/python
# -*- coding: UTF-8 -*-
# file: client.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 8888

s.connect((host, port))
print s.recv(1024)
s.close()
