import pyautogui
import webbrowser
import time


url = 'insert github link here'
webbrowser.open(url)

while True:
    time.sleep(120)
    pyautogui.hotkey('f5')
    print('sending request to %s' %(url))
