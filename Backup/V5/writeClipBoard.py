import win32api, win32clipboard

def Set_Clip_Board(txt: str):
		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardText(txt, win32clipboard.CF_UNICODETEXT)
		win32clipboard.CloseClipboard()

def Read_Clip_Board():
	try:
		win32clipboard.OpenClipboard()
		data = win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()
		return data
	except TypeError as p:
	    return ""

#https://stackoverflow.com/questions/7050448/write-image-to-windows-clipboard-in-python-with-pil-and-win32clipboard

