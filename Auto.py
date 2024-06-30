import pyautogui
import pyscreeze
import time

#To open vscode

pyautogui.hotkey('ctrl', 'shift', 't')
time.sleep(2)
pyautogui.write('code')
time.sleep(2)
pyautogui.press('enter')
time.sleep(4)


#install clangd from extension

pyautogui.hotkey('ctrl', 'shift', 'x')
pyautogui.write('clangd')
pyautogui.press('enter')
pyautogui.moveTo(622, 348,5)
time.sleep(2)
pyautogui.click()
time.sleep(10)

#install c++ testmate from extension

pyautogui.hotkey('ctrl', 'shift', 'x')
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('c++ testmate')
pyautogui.press('enter')
pyautogui.moveTo(622, 348,5)
time.sleep(2)
pyautogui.click()
time.sleep(10)


#install c++ helper from extension

pyautogui.hotkey('ctrl', 'shift', 'x')
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('c++ helper')
pyautogui.press('enter')
pyautogui.moveTo(622, 348,5)
time.sleep(2)
pyautogui.click()
time.sleep(10)


#install cmake from extension

pyautogui.hotkey('ctrl', 'shift', 'x')
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('cmake')
pyautogui.press('enter')
pyautogui.moveTo(622, 348,5)
time.sleep(2)
pyautogui.click()         
pyautogui.moveTo(622, 348,5)


#install cmake tools from extension

pyautogui.hotkey('ctrl', 'shift', 'x')
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('cmake tools')
pyautogui.press('enter')
pyautogui.moveTo(622, 348,5)
time.sleep(2)
pyautogui.click()  
time.sleep(10)       