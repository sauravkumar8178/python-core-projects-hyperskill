import time
import pyautogui

def screenshot():
    name = int(round(time.time()*1000))
    name ='D:\Python\Screen data\{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot('testing.png')
    img.show()

screenshot()
