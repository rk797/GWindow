# Ghostwindow
>A small python package with some useful window utility functions
```python
import ghostwindow

hwnd = ghostwindow.getHWND("Untitled - Notepad")
ghostwindow.hideWindow(hwnd)
```
## Introduction
Ghostwindow is a python window management package built on the ctypes library. It includes some useful utility functions that can be used to set/get window properties easily. Ghostwindow is designed to work on Windows 10+

### Here is what Ghostwindow is Capable of

* Able to fetch hwnd by window title
* Able to exclude window from capture
* Able to exclude window from screenshot
* Able to hide window from task bar & task manager (burries deep in process list)
* Able to show window
* Able to maximize window
* Able to minimize window
* Able to set window transparency
## Installation (From PyPi)
```python
pip install ghostwindow
```
## Usage
Ghostwindow allows you to pass either a hwnd (handle to the window) or the window title itself.
```python
import ghostwindow

hwnd = ghostwindow.getHWND("Untitled - Notepad")
ghostwindow.setWindowTransparency(hwnd, 0.5)
```
```python
import ghostwindow

ghostwindow.setWindowTransparency("Untitled - Notepad", 0.5)
```
### Exclude from capture
Ghostwindow provides a function to exclude a window from screenshot and any capture / screen recording software. To exclude a window from capture, use the excludeCapture() function. The window that is excluded from capture MUST belong to the current process, otherwise it will not work. 
>[!NOTE]
> Console windows do not belong to the current process
```python
import ghostwindow as gw
import tkinter as tk

root = tk.Tk()
root.title("demo")
root.geometry("300x300")

def mainLoop():
    hwnd = gw.getHWND("demo")
    gw.excludeCapture(hwnd)
    while True:
        input()
        
root.after(1000, mainLoop)
root.mainloop()
```
### Fetch properties
Ghostwindow also allows you to fetch window properties
```python
import ghostwindow

title = "Untitled - Notepad"
print(ghostwindow.getWindowSize(title))
print(ghostwindow.getWindowPosition(title))
print(ghostwindow.getWindowProcessId(title))
```
### Complete list of all the functionality ghostwindow provides
```
getHWND(winTitle)
excludeCapture(hwnd)
includeCapture(hwnd)
hideWindow(hwnd)
showWindow(hwnd)
setWindowTransparency(hwnd, trans)
minimizeWindow(hwnd)
maximizeWindow(hwnd)
bringToFront(hwnd)
closeWindow(hwnd)
getWindowSize(hwnd)
getWindowPosition(hwnd)
getWindowProcessId(hwnd)
```
