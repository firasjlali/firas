import pyautogui
import time
import random
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
currentMouseX, currentMouseY
(1314, 345)

pyautogui.moveTo(1000, 20)# Move the mouse to XY coordinates.
pyautogui.click()

pyautogui.moveTo(1000, 50)# Move the mouse to XY coordinates.
pyautogui.click()
pyautogui.write('youtube')
pyautogui.press('enter')
time.sleep(15)
pyautogui.moveTo(70, 550)


pyautogui.click(button='left')
time.sleep(10)
while True:
    pyautogui.moveTo(300, 450)
    time.sleep(10)
    pyautogui.click(button='left')
    pyautogui.moveTo(70, 700)
    time.sleep(random.randint(1,30))
    pyautogui.click(button='left')
    time.sleep(random.randint(12,400))
    pyautogui.moveTo(500, 520)
    pyautogui.click(button='left')
    time.sleep(random.randint(5,56))
    pyautogui.moveTo(70, 700)
    #time.sleep(10)
    pyautogui.click(button='left')
    time.sleep(random.randint(20,550))
    pyautogui.moveTo(700, 520)
    pyautogui.click(button='left')
    time.sleep(random.randint(5,110))
    pyautogui.moveTo(70, 700)
    pyautogui.click(button='left')
    time.sleep(random.randint(20,609))
    pyautogui.moveTo(950, 520)
    pyautogui.click(button='left')
    time.sleep(random.randint(2,20))
    pyautogui.moveTo(70, 700)
    pyautogui.click(button='left')
    time.sleep(random.randint(0,10))
    pyautogui.moveTo(1150, 520)
    pyautogui.click(button='left')
    time.sleep(random.randint(30,600))
    pyautogui.moveTo(70, 700)
    
    #time.sleep(30)
    #pyautogui.click(button='left')
#pyautogui.write('@al_chahin')


#pyautogui.moveTo(730, 630)# Move the mouse to XY coordinates.
#pyautogui.click()
