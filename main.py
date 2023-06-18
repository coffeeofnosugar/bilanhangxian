from PySide6.QtWidgets import QApplication, QWidget
from Ui_MyWindow import Ui_MyWindow
from PySide6.QtCore import QThread, Signal
import time

class WorkThread(QThread):
    signal = Signal()

    def __init__(self):
        super().__init__()
        print("run")
    
    def run(self):
        print("123")
        from win32 import BiLanHangXian, GetImage
        b = BiLanHangXian()
        b.FindTarget(GetImage("./image/test_1.png"), max_time = 5)
        print("456")
        

class MyMainWindow(Ui_MyWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

        
    def bind(self):
        self.workThread = WorkThread()  # 实例化一个线程对象
        self.workThread.started.connect(lambda : print('线程开始了'))
        self.workThread.finished.connect(lambda: print('线程结束了'))
        self.yanxi_button.clicked.connect(lambda : self.workThread.start())
        # self.yanxi_button_4.clicked.connect(lambda : print(self.workThread.currentThread()))  # 同样，也可以使用连接按钮



    def yan_xi(self, timer):
        from win32 import BiLanHangXian
        b = BiLanHangXian()
        b.yan_xi(timer)
        


if __name__ == "__main__":
    app = QApplication()
    myWin = MyMainWindow()
    myWin.show()
    app.exec()