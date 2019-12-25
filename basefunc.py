import win32gui
import win32api
import cv2
import aircv as ac
import pyautogui
import logging
import numpy as np

baseLeft = 0
baseTop = 0
baseRight = 0
baseBottom = 0
baseWidth = 0
baseHeight = 0

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def GetBaseRect(titlename):
	global baseLeft
	global baseTop
	global baseRight
	global baseBottom
	global baseWidth
	global baseHeight
	classname = "MozillaWindowClass"
	#获取句柄
	hwnd = win32gui.FindWindow(0, titlename)
	#获取窗口左上角和右下角坐标
	baseLeft, baseTop, baseRight, baseBottom = win32gui.GetWindowRect(hwnd)
	baseWidth = baseRight - baseLeft
	baseHeight = baseBottom - baseTop
	
def RX(x):
	global baseLeft
	return x + baseLeft

def RY(y):
	global baseTop
	return y + baseTop	

def SimpleClick(x, y):
	pyautogui.moveTo(RX(x), RY(y))
	pyautogui.click()


def SimpleSwipe(x1, y1, x2, y2):
	pyautogui.moveTo(RX(x1), RY(y1), 0.5)
	pyautogui.dragTo(RX(x2), RY(y2), 0.5, button='left')

def FindImageInRect(x1, y1, x2, y2, image, thld):
	src = pyautogui.screenshot(region=[RX(x1), RY(y1), RX(x2) - RX(x1), RY(y2) - RY(y1)])
	#src = cv2.imread("temp.png")
	#src = src[RY(y1):RY(y2), RX(x1):RX(x2)]
	template = cv2.imread(image)
	src = cv2.cvtColor(np.asarray(src), cv2.COLOR_RGB2BGR)
	#cv2.imshow("adsf", src)
	#cv2.waitKey(0)
	res = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
	threshold = thld
	pos = []

	loc = np.where(res >= threshold)
	for pt in zip(*loc[::-1]):
		pos.append(pt)

	if len(pos) == 0:
		return None

	return x1 + pos[0][0] + int(template.shape[1] / 2), y1 + pos[0][1] + int(template.shape[0] / 2)

def FindImageInScreen(image):

	img = pyautogui.screenshot("temp.png")
	src = cv2.imread("temp.png", 0)
	template = cv2.imread(image, 0)
	res = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	pos = []

	loc = np.where(res >= threshold)
	for pt in zip(*loc[::-1]):
		pos.append(pt)

	if len(pos) == 0:
		return None
		
	return pos[0][0] + int(template.shape[1] / 2), pos[0][1] + int(template.shape[0] / 2)

def Log(logStr):
	print(logStr)
	logger.info(logStr)
	
def Error(logStr):
	print(logStr)
	logger.error(logStr)
	