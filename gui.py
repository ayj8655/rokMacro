import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('rok Macro')
        self.setWindowIcon(QIcon('icon.png'))   #타이틀 옆 아이콘이미지 삽입
#        self.move(300, 300)     #스크린의 위치로이동
#        self.resize(400, 200)   #위젯의 크기 조절
        self.setGeometry(300, 300, 300, 200) # 초기 위치 및 크기 지정 한번에

        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())