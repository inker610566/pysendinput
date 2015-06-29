# some c native type
from ctypes import c_int, c_char_p, WINFUNCTYPE, windll, create_string_buffer, byref
# composite type
from ctypes import Structure, Union
# some windows native type
from ctypes.wintypes import HWND, LPCSTR, UINT, LPARAM, BOOL, LONG, WORD, DWORD, LPVOID
ULONG_PTR = LPVOID

import ctypes
from time import sleep

#print ctypes.windll.user32.SendInput
#print hex(ctypes.windll.User32.FindWindowExA(None, None, None, None))
#hwnd = ctypes.windll.User32.FindWindowExA(None, None, None, None)

# c_char_p
#print ctypes.windll.User32.GetClassNameA(hwnd, p, 100)

callback_proto = WINFUNCTYPE(BOOL, HWND, LPARAM)

# sendinput
class MOUSEINPUT(Structure):
	_fields_ = [
		("dx", LONG),
		("dy", LONG),
		("mouseData", DWORD),
		("dwFlags", DWORD),
		("time", DWORD),
		("dwExtraInfo", ULONG_PTR),
	]

class KEYBDINPUT(Structure):
	_fields_ = [
		("wVk", WORD),
		("wScan", WORD),
		("dwFlags", DWORD),
		("time", DWORD),
		("dwExtraInfo", ULONG_PTR),
	]

class HARDWAREINPUT(Structure):
	_fields_ = [
		("uMsg", DWORD),
		("wParamL", WORD),
		("wParamH", WORD),
	]
	
class InputTypeUnion(Union):
	_fields_ = [
		("mi", MOUSEINPUT),
		("ki", KEYBDINPUT),
		("hi", HARDWAREINPUT),
	]

class INPUT(Structure):
	_fields_ = [
		("type" , DWORD),
		("type_input", InputTypeUnion),
	]

def EnumWindowsCallback(hwnd, lparam):
	#p = ctypes.cdll.msvcrt.malloc(c_int(100))
	p = create_string_buffer('\000' * 100)
	ctypes.windll.User32.GetWindowTextA(hwnd, byref(p), 100)
	if p.value.find("Age of Empires") != -1:
		print p.value
		ctypes.windll.User32.SetForegroundWindow(hwnd)
		ctypes.windll.User32.ShowWindow(hwnd, c_int(10))
		#ctypes.windll.User32.SetActiveWindow(hwnd)
		sendinput()
		return 0
	#ctypes.cdll.msvcrt.printf(c_char_p("%s\n"), p)
	#ctypes.cdll.msvcrt.free(p)
	return 1

def sendinput():
	ip = INPUT()
	
	'''
		0 for mouse
		1 for keyboard
		2 for hardware
	'''
	ip.type = DWORD(1)
	ip.type_input.ki.wScan = WORD(0)
	ip.type_input.ki.time = DWORD(0)
	ip.type_input.ki.dwExtraInfo = ULONG_PTR(0)

	sleep(5)
	
	
	for i in range(500):
		# Press the "Ctrl" key
		ip.type_input.ki.wVk = WORD(int("11", 16))
		ip.type_input.ki.dwFlags = DWORD(0)
		ctypes.windll.User32.SendInput(UINT(1), byref(ip), c_int(ctypes.sizeof(ip)))
		
		ip.type_input.ki.wVk = WORD(int("56", 16))
		ip.type_input.ki.dwFlags = DWORD(0)
		ctypes.windll.User32.SendInput(UINT(1), byref(ip), c_int(ctypes.sizeof(ip)))
		
		ip.type_input.ki.wVk = WORD(int("56", 16))
		ip.type_input.ki.dwFlags = DWORD(2)
		ctypes.windll.User32.SendInput(UINT(1), byref(ip), c_int(ctypes.sizeof(ip)))
		
		ip.type_input.ki.wVk = WORD(int("11", 16))
		ip.type_input.ki.dwFlags = DWORD(2)
		ctypes.windll.User32.SendInput(UINT(1), byref(ip), c_int(ctypes.sizeof(ip)))
		
		sleep(0.1)
		
		# Enter
		ip.type_input.ki.wVk = WORD(13)
		ip.type_input.ki.dwFlags = DWORD(0)
		ctypes.windll.User32.SendInput(UINT(1), byref(ip), c_int(ctypes.sizeof(ip)))
		
		# Enter
		ip.type_input.ki.wVk = WORD(13)
		ip.type_input.ki.dwFlags = DWORD(2)
		ctypes.windll.User32.SendInput(UINT(1), byref(ip), c_int(ctypes.sizeof(ip)))
		
		sleep(0.1)
	
		# Enter
		ip.type_input.ki.wVk = WORD(13)
		ip.type_input.ki.dwFlags = DWORD(0)
		ctypes.windll.User32.SendInput(UINT(1), byref(ip), c_int(ctypes.sizeof(ip)))
		
		# Enter
		ip.type_input.ki.wVk = WORD(13)
		ip.type_input.ki.dwFlags = DWORD(2)
		ctypes.windll.User32.SendInput(UINT(1), byref(ip), c_int(ctypes.sizeof(ip)))
		
		sleep(0.1)
		
callback = callback_proto(EnumWindowsCallback)
	
ctypes.windll.User32.EnumWindows(callback, LPARAM(0))
	
	
	
'''
	windows native type
["ARRAY", "ATOM", "ArgumentError", "Array", "BOOL", "BOOLEAN", "BYTE", "BigEndianStructure", "CDLL", "CFUNCTYPE", "COLORREF", "DEFAULT_MODE", "DOUBLE", "DWORD", "DllCanUnloadNow", "DllGetClassObject", "FILETIME", "FLOAT", "FormatError", "GetLastError", "HACCEL", "HANDLE", "HBITMAP", "HBRUSH", "HCOLORSPACE", "HDC", "HDESK", "HDWP", "HENHMETAFILE", "HFONT", "HGDIOBJ", "HGLOBAL", "HHOOK", "HICON", "HINSTANCE", "HKEY", "HKL", "HLOCAL", "HMENU", "HMETAFILE", "HMODULE", "HMONITOR", "HPALETTE", "HPEN", "HRESULT", "HRGN", "HRSRC", "HSTR", "HTASK", "HWINSTA", "HWND", "INT", "LANGID", "LARGE_INTEGER", "LCID", "LCTYPE", "LGRPID", "LONG", "LPARAM", "LPCOLESTR", "LPCSTR", "LPCVOID", "LPCWSTR", "LPOLESTR", "LPSTR", "LPVOID", "LPWSTR", "LibraryLoader", "LittleEndianStructure", "MAX_PATH", "MSG", "OLESTR", "OleDLL", "POINT", "POINTER", "POINTL", "PYFUNCTYPE", "PyDLL", "RECT", "RECTL", "RGB", "RTLD_GLOBAL", "RTLD_LOCAL", "SC_HANDLE", "SERVICE_STATUS_HANDLE", "SHORT", "SIZE", "SIZEL", "SMALL_RECT", "SetPointerType", "Structure", "UINT", "ULARGE_INTEGER", "ULONG", "USHORT", "Union", "VARIANT_BOOL", "WCHAR", "WIN32_FIND_DATAA", "WIN32_FIND_DATAW", "WINFUNCTYPE", "WORD", "WPARAM", "WinDLL", "WinError", "_COORD", "_FILETIME", "_LARGE_INTEGER", "_POINTL", "_RECTL", "_SMALL_RECT", "_SimpleCData", "_ULARGE_INTEGER", "__all__", "__builtins__", "__doc__", "__file__", "__name__", "__package__", "addressof", "alignment", "byref", "c_bool", "c_buffer", "c_byte", "c_char", "c_char_p", "c_double", "c_float", "c_int", "c_int16", "c_int32", "c_int64", "c_int8", "c_long", "c_longdouble", "c_longlong", "c_short", "c_size_t", "c_ssize_t", "c_ubyte", "c_uint", "c_uint16", "c_uint32", "c_uint64", "c_uint8", "c_ulong", "c_ulonglong", "c_ushort", "c_void_p", "c_voidp", "c_wchar", "c_wchar_p", "cast", "cdll", "create_string_buffer", "create_unicode_buffer", "get_errno", "get_last_error", "memmove", "memset", "oledll", "pointer", "py_object", "pydll", "pythonapi", "resize", "set_conversion_mode", "set_errno", "set_last_error", "sizeof", "string_at", "tagMSG", "tagPOINT", "tagRECT", "tagSIZE", "windll", "wstring_at"]
'''
