import ctypes
import time
import os
import ctypes.wintypes

def getHWND(_hwnd):
    try:
        if isinstance(_hwnd, int):
            h = _hwnd
        else:
            h = ctypes.windll.user32.FindWindowW(None, _hwnd)

        if h != 0:
            return h
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(3)
        os._exit(1)

def hideWindow(_hwnd):
    try:
        h = getHWND(_hwnd)
        if h != 0:
            ctypes.windll.user32.ShowWindow(h, 0)  # SW_HIDE
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(3)
        os._exit(1)

def showWindow(_hwnd):
    try:
        h = getHWND(_hwnd)
        if h != 0:
            ctypes.windll.user32.ShowWindow(h, 1)  # SW_SHOWNORMAL
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(3)
        os._exit(1)

def getWindowSize(_hwnd):
    try:
        h = getHWND(_hwnd)
        if h != 0:
            rect = ctypes.wintypes.RECT()
            ctypes.windll.user32.GetWindowRect(h, ctypes.byref(rect))
            width = rect.right - rect.left
            height = rect.bottom - rect.top
            return width, height
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")
        return None

def getWindowPosition(_hwnd):
    try:
        h = getHWND(_hwnd)
        if h != 0:
            rect = ctypes.wintypes.RECT()
            ctypes.windll.user32.GetWindowRect(h, ctypes.byref(rect))
            x, y = rect.left, rect.top
            return x, y
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")
        return None

def getWindowProcessId(_hwnd):
    try:
        h = getHWND(_hwnd)
        if h != 0:
            process_id = ctypes.wintypes.DWORD()
            ctypes.windll.user32.GetWindowThreadProcessId(h, ctypes.byref(process_id))
            return process_id.value
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")
        return None

def minimizeWindow(_hwnd):
    try:
        h = getHWND(_hwnd)
        if h != 0:
            ctypes.windll.user32.ShowWindow(h, 6)  # SW_MINIMIZE
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(3)
        os._exit(1)

def maximizeWindow(_hwnd):
    try:
        h = getHWND(_hwnd)
        if h != 0:
            ctypes.windll.user32.ShowWindow(h, 3)  # SW_MAXIMIZE
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(3)
        os._exit(1)

def bringToFront(_hwnd):
    try:
        h = getHWND(_hwnd)
        if h != 0:
            ctypes.windll.user32.ShowWindow(h, 9)  # SW_RESTORE
            ctypes.windll.user32.SetForegroundWindow(h)
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")

def setWindowTransparency(_hwnd, transparency):
    try:
        h = getHWND(_hwnd)
        if h != 0:
            style = ctypes.windll.user32.GetWindowLongW(h, -20)  # GWL_EXSTYLE
            if not style & 0x80000:  # WS_EX_LAYERED
                ctypes.windll.user32.SetWindowLongW(h, -20, style | 0x80000)  # WS_EX_LAYERED

            ctypes.windll.user32.SetLayeredWindowAttributes(h, 0, int(255 * transparency), 2)  # LWA_ALPHA
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")

def closeWindow(_hwnd):
    try:
        h = getHWND(_hwnd)
        if h != 0:
            ctypes.windll.user32.PostMessageW(h, 0x10, 0, 0)  # WM_CLOSE
        else:
            raise Exception("Window not found.")
    except Exception as e:
        print(f"Error: {e}")


def excludeCapture(_hwnd):
    HWND = getHWND(_hwnd)
    # WDA_NONE = 0x00000000
    WDA_EXCLUDEFROMCAPTURE = 0x00000011

    SetWindowDisplayAffinity = ctypes.windll.user32.SetWindowDisplayAffinity
    SetWindowDisplayAffinity.argtypes = [ctypes.wintypes.HWND, ctypes.wintypes.DWORD]
    SetWindowDisplayAffinity.restype = ctypes.wintypes.BOOL


    if SetWindowDisplayAffinity(HWND, WDA_EXCLUDEFROMCAPTURE):
        pass
    else:
        error_code = ctypes.windll.kernel32.GetLastError()
        print(f"Failed to set window display affinity. Error code: {error_code}")
        if error_code == 5:
            print("Access denied. Window must belong to the current process.")
        ctypes.windll.kernel32.FormatMessageW.restype = ctypes.wintypes.DWORD
        ctypes.windll.kernel32.FormatMessageW.argtypes = [
            ctypes.wintypes.DWORD, ctypes.wintypes.LPCVOID, ctypes.wintypes.DWORD,
            ctypes.wintypes.DWORD, ctypes.wintypes.LPWSTR, ctypes.wintypes.DWORD,
            ctypes.wintypes.LPVOID
        ]
        message_buffer = ctypes.create_unicode_buffer(256)
        ctypes.windll.kernel32.FormatMessageW(
            0x00001000 | 0x00000200, None, error_code, 0, message_buffer,
            ctypes.sizeof(message_buffer) // ctypes.sizeof(ctypes.wintypes.WCHAR), None
        )
        print(f"Error message: {message_buffer.value}")