import pyautogui
import time

#   moveTo = 마우스 커서 이동 , moveRel = 기존 마우스 위치에서 지정된만큼 이동
#   click = 클릭(인자로 위치 넣으면 무브따로 안해도 바로감), doubleClick() = 더블클릭
#   typewrite('ggg') = 키보드 입력, typewrite(['enter']) = 키보드의 키들중 enter키만 누름
#   locateOnScreen('') = 화면에서 찾아서 위치, 크기 반환, locateCenterOnScreen = 찾아서 센터 바로 반환
#   center() = 센터값 반환


confi = 0.8

while(1):
    handshake = pyautogui.locateCenterOnScreen('handshake.PNG', confidence = confi)
    food = pyautogui.locateCenterOnScreen('food.PNG', confidence = confi)
    wood = pyautogui.locateCenterOnScreen('wood.PNG', confidence = confi)
    stone = pyautogui.locateCenterOnScreen('stone.PNG', confidence = confi)
    gold = pyautogui.locateCenterOnScreen('gold.PNG', confidence = confi)

    print(handshake, food, wood, stone, gold)

    if handshake is not None:
        pyautogui.moveTo(handshake)
        pyautogui.moveRel(0,40)
        pyautogui.click()
        print("악수 자동으로 했음")
        time.sleep(1)
    if food is not None:
        pyautogui.moveTo(food)
        pyautogui.moveRel(0,40)
        pyautogui.click()
        print("식량 자동으로 했음")
        time.sleep(1)
    if gold is not None:
        pyautogui.moveTo(gold)
        pyautogui.moveRel(0,40)
        pyautogui.click()
        print("금 자동으로 했음")
        time.sleep(1)       
    if wood is not None:
        pyautogui.moveTo(wood)
        pyautogui.moveRel(0,40)
        pyautogui.click()
        print("나무 자동으로 했음")
        time.sleep(1)    
    if stone is not None:
        pyautogui.moveTo(stone)
        pyautogui.moveRel(0,40)
        pyautogui.click()
        print("돌 자동으로 했음")
        time.sleep(1)            
    time.sleep(2)



