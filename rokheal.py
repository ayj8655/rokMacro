import pyautogui, pyperclip
import time

confi = 0.81000
my_msg = 1500    #훈련량
pyautogui.PAUSE = 0.5
pyperclip.copy(my_msg)  #클립보드 저장

#공성유닛 훈련 매크로

while(1):
    time.sleep(3)
    traning9 = pyautogui.locateCenterOnScreen('handshake.PNG', confidence = confi)
    print(traning9)

    if traning9 is not None:
        pyautogui.moveTo(traning9)
        pyautogui.moveRel(0,40)
        pyautogui.click()
        print("악수 클릭 자동")
        time.sleep(1)
1500

    traning = pyautogui.locateCenterOnScreen('heal1.PNG', confidence = confi)
    print(traning)

    if traning is not None:
        pyautogui.moveTo(traning)
        pyautogui.click()
        print("heal1 클릭 자동")
        time.sleep(1)

    traning2 = pyautogui.locateCenterOnScreen('heal2.PNG', confidence = confi)
    print(traning2)

    if traning2 is not None:
        pyautogui.moveTo(traning2)
        pyautogui.moveRel(50,0)
        pyautogui.click()
        print("heal2 클릭 자동")
        time.sleep(1)

    pyperclip.copy(my_msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')
    time.sleep(1)

    traning5 = pyautogui.locateCenterOnScreen('heal3.PNG', confidence = confi)
    print(traning5)
    
    if traning5 is not None:
        pyautogui.moveTo(traning5)
        pyautogui.click()
        print("heal3 자동으로 했음")
        time.sleep(1)

    traning6 = pyautogui.locateCenterOnScreen('heal4.PNG', confidence = confi)
    print(traning6)

    if traning6 is not None:
        pyautogui.moveTo(traning6)
        pyautogui.click()
        print("heal4 자동")
        time.sleep(1)
    

    traning7 = pyautogui.locateCenterOnScreen('heal5.PNG', confidence = confi)
    print(traning7)

    if traning7 is not None:
        pyautogui.moveTo(traning7)
        pyautogui.click()
        print("heal5 자동")
        time.sleep(1)













