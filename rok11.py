import pyautogui, pyperclip
import time

confi = 0.8
my_msg = 324    #훈련량
pyautogui.PAUSE = 0.5
pyperclip.copy(my_msg)  #클립보드 저장

#공성유닛 훈련 매크로

while(1):

    traning = pyautogui.locateCenterOnScreen('traning.PNG', confidence = confi)
    print(traning)

    if traning is not None:
        pyautogui.moveTo(traning)
        pyautogui.click()
        print("최초 클릭 자동")

    traning2 = pyautogui.locateCenterOnScreen('traning2.PNG', confidence = confi)
    print(traning2)

    if traning2 is not None:
        pyautogui.moveTo(traning2)
        pyautogui.click()
        print("두번째 클릭 자동")

    traning3 = pyautogui.locateCenterOnScreen('traning3.PNG', confidence = confi)
    print(traning3)
    
    if traning3 is not None:
        pyautogui.moveTo(traning3)
        pyautogui.click()
        print("세번째 자동으로 했음")
    traning4 = pyautogui.locateCenterOnScreen('traning4.PNG', confidence = confi)
    print(traning4)

    if traning4 is not None:
        pyautogui.moveTo(traning4)
        pyautogui.click()
        print("네번째 자동으로 했음")

    pyperclip.copy(my_msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')

    traning5 = pyautogui.locateCenterOnScreen('traning5.PNG', confidence = confi)
    print(traning5)
    
    if traning5 is not None:
        pyautogui.moveTo(traning5)
        pyautogui.click()
        print("다섯번 자동으로 했음")
        time.sleep(1)
        pyautogui.moveTo(traning)
        pyautogui.click()
        print("6 클릭 자동")

    traning6 = pyautogui.locateCenterOnScreen('traning6.PNG', confidence = confi)
    print(traning6)

    if traning6 is not None:
        pyautogui.moveTo(traning6)
        pyautogui.click()
        print("7 클릭 자동")

    traning7 = pyautogui.locateCenterOnScreen('traning7.PNG', confidence = confi)
    print(traning7)

    if traning7 is not None:
        pyautogui.moveTo(traning7)
        pyautogui.moveRel(500,0)
        pyautogui.click()
        print("8 클릭 자동")

    traning8 = pyautogui.locateCenterOnScreen('traning8.PNG', confidence = confi)
    print(traning8)

    if traning8 is not None:
        pyautogui.moveTo(traning8)
        pyautogui.click()
        print("9 클릭 자동")














