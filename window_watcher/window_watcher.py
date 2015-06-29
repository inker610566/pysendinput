# some c native type
from ctypes import c_int, c_char_p, WINFUNCTYPE, windll, create_string_buffer, byref
# composite type
from ctypes import Structure, Union
# some windows native type
from ctypes.wintypes import HWND, LPCSTR, UINT, LPARAM, BOOL, LONG, WORD, DWORD, LPVOID
ULONG_PTR = LPVOID

import ctypes


class WindowWatcher:
	def __init__(self, windowTextPatten):
		this.pattern = windowTextPatten
	
	@staticmethod
	def ListCurrentWindows():
		callback_proto = WINFUNCTYPE(BOOL, HWND, LPARAM)
		callback = callback_proto(WindowWatcher._PrintWindowsCallback)
		ctypes.windll.User32.EnumWindows(callback, LPARAM(0))

	@staticmethod
	def _GetWindowDCCallback(hwnd, lparam):
		pass

	@staticmethod
	def _PrintWindowsCallback(hwnd, lparam):
		p = ctypes.cdll.msvcrt.malloc(c_int(100))
		ctypes.windll.User32.GetWindowTextA(hwnd, p, 100)
		ctypes.cdll.msvcrt.printf(c_char_p("%s\n"), p)
		ctypes.cdll.msvcrt.free(p)
		return 1
