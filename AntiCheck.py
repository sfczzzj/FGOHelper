import time
import random
import numpy
import basefunc

def RandomSleep(Delay=None):
	if Delay == None:
		time.sleep(random.randint(400,900) / 1000)
	if Delay == 1:
		time.sleep(random.randint(100,300) / 1000)
	if Delay == 2:
		time.sleep(random.randint(300,500) / 1000)
	if Delay == 3:
		time.sleep(random.randint(500,700) / 1000)
	if Delay == 4:
		time.sleep(random.randint(700,900) / 1000)

def RandomPoint(x, y, r):
	randR = random.randint(0, r)
	randArc = random.randint(0, 360)
	randX = numpy.sin(randArc) * randR
	randY = numpy.cos(randArc) * randR
	return int(round(x + randX)), int(round(y + randY))

def RandomClickOnce():
		RangeClick(int(basefunc.baseWidth / 2), int(basefunc.baseHeight / 2), int(basefunc.baseHeight / 2 - 100))
		
def RandomClick():
	i = random.randint(0, 2)
	for n in range(0, i): 
		RandomClickOnce()

def RangeClick(x, y, r):
	x1, y1 = RandomPoint(x, y, r)
	basefunc.SimpleClick(x1, y1)
	
def RangeSwipe(x1, y1, r1, x2, y2, r2):
	x1, y1 = RandomPoint(x1, y1, r1)
	x2, y2 = RandomPoint(x2, y2, r2)
	basefunc.SimpleSwipe(x1, y1, x2, y2)
	