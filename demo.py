import ghostwindow as gw
import tkinter as tk


# Creates a demo window that belongs to the current process
root = tk.Tk()
root.title("demo")
root.geometry("300x300")
windowTitle = "demo"


def mainLoop():
    while True:
        option = input("(1) Hide window\n(2) Show window\n(3) Set window transparency\n(4) Reset window transparency\n(5) Exclude window from capture\n(6) Minimize window\n(7) Maximize window\n(8) Bring window to front\n(9) Close window\nEnter option:")
        match option:
            case "1":
                gw.hideWindow(windowTitle)
            case "2":
                gw.showWindow(windowTitle)
            case "3":
                gw.setWindowTransparency(windowTitle, 0.3)
            case "4":
                gw.setWindowTransparency(windowTitle, 1.0)
            case "5":
                gw.excludeCapture(windowTitle)
            case "6":
                gw.minimizeWindow(windowTitle)
            case "7":
                gw.maximizeWindow(windowTitle)
            case "8":
                gw.bringToFront(windowTitle)
            case "9":
                gw.closeWindow(windowTitle)
                exit()
            case _:
                print("Invalid option")

# Schedule the mainLoop function to be called after certain period
root.after(300, mainLoop)
root.mainloop()