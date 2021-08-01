import pyautogui
import webbrowser
import time


url = 'https://github.com/robiot'
webbrowser.open(url)

while True:
    time.sleep(20)
    pyautogui.hotkey('f5')
    print('sending request to %s' %(url))
