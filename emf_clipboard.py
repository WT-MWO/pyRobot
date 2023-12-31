from __future__ import print_function
import ctypes
import ctypes.wintypes as w

CF_UNICODETEXT = 13
CF_ENHMETAFILE = 14
CF_METAFILEPICT = 3

u32 = ctypes.WinDLL("user32")
k32 = ctypes.WinDLL("kernel32")

OpenClipboard = u32.OpenClipboard
OpenClipboard.argtypes = (w.HWND,)
OpenClipboard.restype = w.BOOL
GetClipboardData = u32.GetClipboardData
GetClipboardData.argtypes = (w.UINT,)
GetClipboardData.restype = w.HANDLE
GlobalLock = k32.GlobalLock
GlobalLock.argtypes = (w.HGLOBAL,)
GlobalLock.restype = w.LPVOID
GlobalUnlock = k32.GlobalUnlock
GlobalUnlock.argtypes = (w.HGLOBAL,)
GlobalUnlock.restype = w.BOOL
CloseClipboard = u32.CloseClipboard
CloseClipboard.argtypes = None
CloseClipboard.restype = w.BOOL


# def get_clipboard_text():
#     text = ""
#     if OpenClipboard(None):
#         h_clip_mem = GetClipboardData(CF_UNICODETEXT)
#         text = ctypes.wstring_at(GlobalLock(h_clip_mem))
#         GlobalUnlock(h_clip_mem)
#         CloseClipboard()
#     return text

# This is not working, need to understand deeply the C structures to cast the PrntInt


def get_clipboard_emf():
    # text = ""
    meta = w.HMETAFILE
    if OpenClipboard(None):
        h_clip_mem = GetClipboardData(CF_ENHMETAFILE)
        meta = w.HMETAFILE(GlobalLock(h_clip_mem))
        GlobalUnlock(h_clip_mem)
        CloseClipboard()
    return meta


print(get_clipboard_emf())
