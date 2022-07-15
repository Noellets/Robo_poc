#!/usr/bin/env python3
# File name   : servo.py
# Description : Control Servos
# Author      : William
# Date        : 2019/02/23
from __future__ import division
import time
import RPi.GPIO as GPIO
import sys
import Adafruit_PCA9685
import ultra



pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

pwm0_init = 300
pwm0_max  = 430
pwm0_min  = 260
pwm0_pos  = pwm0_init

pwm1_init = 300
pwm1_max  = 380
pwm1_min  = 220
pwm1_pos  = pwm1_init

pwm2_init = 300
pwm2_max  = 370
pwm2_min  = 205
pwm2_pos  = pwm2_init

pwm3_init = 300
pwm3_max  = 420
pwm3_min  = 260
pwm3_pos  = pwm3_init

pwm4_init = 300
pwm4_max  = 340
pwm4_min  = 150
pwm4_pos  = pwm4_init

org_pos = 300



def check_range(raw, max_genout, min_genout):
	if raw > max_genout:
		raw_output = max_genout
	elif raw < min_genout:
		raw_output = min_genout
	else:
		raw_output = raw
	return int(raw_output)


def direcaoleft(speed):
	global pwm0_pos
	pwm0_pos += speed
	pwm0_pos = check_range(pwm0_pos, pwm0_max, pwm0_min)
	pwm.set_pwm(0, 0, pwm0_pos)
	print(pwm0_pos)

def direcaoright(speed):
	global pwm0_pos
	pwm0_pos -= speed
	pwm0_pos = check_range(pwm0_pos, pwm0_max, pwm0_min)
	pwm.set_pwm(0, 0, pwm0_pos)
	print(pwm0_pos)


def armleft(speed):
	global pwm1_pos
	pwm1_pos += speed
	pwm1_pos = check_range(pwm1_pos, pwm1_max, pwm1_min)
	pwm.set_pwm(1, 0, pwm1_pos)
	print(pwm1_pos)

def armright(speed):
	global pwm1_pos
	pwm1_pos -= speed
	pwm1_pos = check_range(pwm1_pos, pwm1_max, pwm1_min)
	pwm.set_pwm(1, 0, pwm1_pos)
	print(pwm1_pos)


def armup(speed):
	global pwm2_pos
	pwm2_pos += speed
	pwm2_pos = check_range(pwm2_pos, pwm2_max, pwm2_min)
	pwm.set_pwm(2, 0, pwm2_pos)
	print(pwm2_pos)

def armdown(speed):
	global pwm2_pos
	pwm2_pos -= speed
	pwm2_pos = check_range(pwm2_pos, pwm2_max, pwm2_min)
	pwm.set_pwm(2, 0, pwm2_pos)
	print(pwm2_pos)


def handup(speed):
	global pwm3_pos
	pwm3_pos += speed
	pwm3_pos = check_range(pwm3_pos, pwm3_max, pwm3_min)
	pwm.set_pwm(3, 0, pwm3_pos)
	print(pwm3_pos)

def handdown(speed):
	global pwm3_pos
	pwm3_pos -= speed
	pwm3_pos = check_range(pwm3_pos, pwm3_max, pwm3_min)
	pwm.set_pwm(3, 0, pwm3_pos)
	print(pwm3_pos)


def grab(speed):
	global pwm4_pos
	pwm4_pos -= speed
	pwm4_pos = check_range(pwm4_pos, pwm4_max, pwm4_min)
	pwm.set_pwm(4, 0, pwm4_pos)
	print(pwm4_pos)

def loose(speed):
	global pwm4_pos
	pwm4_pos += speed
	pwm4_pos = check_range(pwm4_pos, pwm4_max, pwm4_min)
	pwm.set_pwm(4, 0, pwm4_pos)
	print(pwm4_pos)


def servo_init():
	pwm.set_pwm(0, 0, pwm0_pos)
	pwm.set_pwm(1, 0, pwm1_pos)
	pwm.set_pwm(2, 0, pwm2_pos)
	pwm.set_pwm(3, 0, pwm3_pos)
	pwm.set_pwm(4, 0, pwm4_pos)


def clean_all():
	global pwm
	pwm = Adafruit_PCA9685.PCA9685()
	pwm.set_pwm_freq(50)
	pwm.set_all_pwm(0, 0)


def ahead():
	global pwm0_pos, pwm1_pos
	pwm.set_pwm(0, 0, pwm0_init)
	pwm.set_pwm(1, 0, (pwm1_max-20))
	pwm0_pos = pwm0_init
	pwm1_pos = pwm1_max-20


def get_direction():
	return (pwm0_pos - pwm0_init)

'''
if __name__ == '__main__':
	#while 1:
		for i in range(0,100,10):
			print("Valor maximo: ", 300 + i)
			pwm.set_pwm(0, 0, (300+i))
			time.sleep(1)


		#for i in range(0,100,10):
			#print("Valor minimo: ", 300 - i)
			#pwm.set_pwm(0, 0, (300-i))
			#time.sleep(0.05)
			
'''
