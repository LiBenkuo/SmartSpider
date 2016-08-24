# -*- coding: UTF-8 -*-

class Room:

  '房间类' # 类文档字符串

  def __init__():
    pass

  def __del__(self):
    class_name = self.__class__.__name__
    print class_name, "销毁"
