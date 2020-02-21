import pyautogui, time, pyperclip, random, sys

#자체 딜레이
def set_delay():
    delay_time = input("몇 초 후에 프로그램을 실행하시겠습니까? : ")
    print(delay_time + "초 후에 프로그램을 실행합니다.")
    for remaining in range(int(delay_time), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r프로그램 실행!\n")

my_msg = '테스트용'
pyautogui.PAUSE = 1 # pyautogui 자체 딜레이 거는 용도

person = pyautogui.locateCenterOnScreen('person.png', confidence = 0.8)
pyautogui.click(person)
pyautogui.keyDown('enter')
pyperclip.copy(my_msg)  # 값을 클립보드에 저장
pyautogui.hotkey('ctrl', 'v')
pyautogui.keyDown('enter')
pyautogui.keyDown('esc')

