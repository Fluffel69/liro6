import pyautogui
import keyboard
x=input()
if x =='поиск':
    c=input()
    pyautogui.moveTo(200,1080)
    pyautogui,click()
    pyautogui.write(c)
    pyautogui.press('enter')
elif x=='текст':
    c=input('Enter your recuest')
    pyautogui.moveTo(1750,20)
    pyautogui.click()
    pyautogui.doubleClick()
    pyautogui.write(c)
elif x=='выход':
    pyautogui.moveTo(1750,20)
    pyautogui.click()
else:
    print('неизвестная команда')