from ctypes.wintypes import HWND
from ctypes.windll import User32 as User32dll
from ctypes import WINFUNCTYPE

import re

WINDOW_NAME_LENGTH = 100

class Window:
	def __init__(self, hwnd):
		self.hwnd = hwnd

'''
	@param regex re.compile('xxx')
	@return a Window object
'''
def FindWindowByName(regex):

	if regex.find()

def _EnumWindowsCallback(hwnd, lparam):
	global WINDOW_NAME_LENGTH
	p = create_string_buffer('\000' * WINDOW_NAME_LENGTH)
	User32dll.GetWindowTextA(hwnd, byref(p), WINDOW_NAME_LENGTH)

'''
	https://msdn.microsoft.com/zh-tw/library/windows/desktop/ms633497(v=vs.85).aspx
	@param match_func
'''
def _PrepareFindWindowByName(match_func):
	# callback_proto
	WNDENUMPROC = WINFUNCTYPE(BOOL, HWND, LPARAM)

	# gen callback
	callback = WNDENUMPROC(_EnumWindowsCallback)

	User32dll.EnumWindows(callback, point(match_func))

