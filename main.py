from win32 import BiLanHangXian, GetImage
from PySide6.QtWidgets import QApplication, QWidget
from Ui_MyWindow import Ui_MyWindow
from PySide6.QtCore import QObject, QThread, Signal
import time



class WorkThread(QObject):
    signal = Signal()

    def __init__(self):
        super().__init__()
        print("run")

    def moveToThread(self, thread: QThread) -> None:
        super().moveToThread(thread)
        self.thread = thread

    def Exit(func):
        '''
        在执行完函数后，结束线程
        '''
        def wrapper(self):
            result = func(self)
            self.thread.exit()
            return result
        return wrapper

    @Exit
    def FindTarget(self):
        b.FindTarget(GetImage("./image/test_1.png"), max_time = 5)
    
    @Exit
    def yan_xi(self):
        b.yan_xi(10)
        

    

class MyMainWindow(Ui_MyWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

        
    def bind(self):


        # FindTarget
        self.workThread = WorkThread()  # 实例化一个工作线程对象
        self.threadList = QThread()  # 实例化一个线程池对象
        self.workThread.moveToThread(self.threadList)  # 将工作线程移动到子线程中
        self.threadList.started.connect(self.workThread.FindTarget)
        self.threadList.finished.connect(lambda: print('finished'))
        self.yanxi_button_0.clicked.connect(self.threadList.start)

        # yan_xi
        self.yanxiThread = WorkThread()  # 实例化一个工作线程对象
        self.yanxiList = QThread()
        self.yanxiThread.moveToThread(self.yanxiList)  # 将工作线程移动到子线程中 （
        self.yanxiList.started.connect(self.yanxiThread.yan_xi)  # 将工作线程移动到子线程中
        self.yanxiList.finished.connect(lambda: print('yan_xi finished'))  # 连接结束条件，在finished条件下，执行下
        self.yanxi_button_1.clicked.connect(self.yanxiList.start)


if __name__ == "__main__":
    b = BiLanHangXian()
    app = QApplication()
    myWin = MyMainWindow()
    myWin.show()
    app.exec()