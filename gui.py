import sys, pyautogui, time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.statusBar().showMessage('Ready')   #상태바


        QToolTip.setFont(QFont('SansSerif', 10))    #폰트설정
        self.setToolTip('This is a <b>QWidget</b> 창')  #창 툴팁
        
        btn = QPushButton('Quit', self)     #버튼생성
        btn.move(50, 50)                    #위치 조정

        btn.setToolTip('This is a <b>QPushButton</b> 버튼')   #버튼 툴팁

        btn.resize(btn.sizeHint())

        btn.clicked.connect(abcde)   #이벤트리스너연결
        self.setWindowTitle('rok Macro')
        self.setWindowIcon(QIcon('icon.png'))   #타이틀 옆 아이콘이미지 삽입
#        self.move(300, 300)     #스크린의 위치로이동
#        self.resize(400, 200)   #위젯의 크기 조절
        self.setGeometry(300, 300, 300, 200) # 초기 위치 및 크기 지정 한번에
        self.show()


    def ararm(self):
        print(pyautogui.position())

def babas():
    print(pyautogui.position())

def abcde():
    confi = 0.8 #정확도
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



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())