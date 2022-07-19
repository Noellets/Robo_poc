#!/usr/bin/env/python3
# File name   : server.py
# Description : for OLED functions
# Website	 : www.gewbot.com
# Author	  : William(Based on Adrian Rosebrock's OpenCV code on pyimagesearch.com)
# Date		: 2019/08/28

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time
import threading

try:
	serial = i2c(port=1, address=0x3C)
	device = ssd1306(serial, rotate=0)
except:
	print('OLED disconnected\nOLED没有连接')

# Box and text rendered in portrait mode
# with canvas(device) as draw:
# 	draw.text((0, 0), "WWW.CODELECTRON.COM", fill="white")
# 	draw.text((0, 10), "WWW.CODELECTRON.COM", fill="white")
# 	draw.text((0, 20), "WWW.CODELECTRON.COM", fill="white")
# 	draw.text((0, 30), "WWW.CODELECTRON.COM", fill="white")
# 	draw.text((0, 40), "WWW.CODELECTRON.COM", fill="white")
# 	draw.text((0, 50), "WWW.CODELECTRON.COM", fill="white")
# while 1:
# 	time.sleep(1)

text_1 = '------------------'
text_2 = '------------------'
text_3 = '------------------'
text_4 = '------------------'
text_5 = '------------------'
text_6 = '------------------'

class OLED_ctrl:
	def __init__(self):
		self.run()

	def run(self):
		print("RUN")
		with canvas(device) as draw:
			draw.text((0, 0), text_1, fill="white")
			draw.text((0, 10), text_2, fill="white")
			draw.text((0, 20), text_3, fill="white")
			draw.text((0, 30), text_4, fill="white")
			draw.text((0, 40), text_5, fill="white")
			draw.text((0, 50), text_6, fill="white")
			

	def screen_show(self, position, text):
		print('SCREEN SHOW', text)
		global text_1, text_2, text_3, text_4, text_5, text_6
		if position == 1:
			text_1 = text
		elif position == 2:
			text_2 = text
		elif position == 3:
			text_3 = text
		elif position == 4:
			text_4 = text
		elif position == 5:
			text_5 = text
		elif position == 6:
			text_6 = text
		self.run()


'''
if __name__ == '__main__':
	screen = OLED_ctrl()
	screen.start()
	screen.screen_show(1, 'ADEEPT.COM')
	while 1:
		time.sleep(10)
		pass
'''
