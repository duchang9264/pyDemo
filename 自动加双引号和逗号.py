# -*- coding:utf-8 -*-
import pyperclip

s = pyperclip.paste()
list_ = [ '\"' + i +'\"' + ',' for i in s.split('\r\n') if i]
s_ = '\n'.join(list_)[:-1]
#s_ = '\n'.join(list_)
pyperclip.copy(s_)
print(s_)