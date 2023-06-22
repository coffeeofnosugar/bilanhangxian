from win32 import BiLanHangXian, GetImage
from PySide6.QtWidgets import QApplication, QWidget
from Ui_MyWindow import Ui_MyWindow
from PySide6.QtCore import QObject, QThread, Signal
import time



class WorkThread(QObject):
    signal = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        print("run")

    def moveToThread(self, thread: QThread) -> None:
        super().moveToThread(thread)
        self.thread = thread

    def Exit(func):
        '''
        在执行完函数后，结束线程
        '''
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            self.thread.exit()
            return result
        return wrapper

    # @Exit
    # def FindTarget(self):
    #     b.FindTarget(GetImage("./image/test_1.png"), max_time = 5)
    
    @Exit
    def yan_xi(self):
        print(self.kwargs['timer'], "次")
        b.yan_xi(self.kwargs['timer'])
        # for i in range(self.kwargs['timer']):
        #     print(i)
        #     time.sleep(1)
        

    

class MyMainWindow(Ui_MyWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

        
    def bind(self):
        # yan_xi
        self.yanxiThread = QThread()
        self.yanxiThread.finished.connect(lambda: print('yan_xi finished'))
        self.yanxi_button_0.clicked.connect(self.yanxi_thread)
        
    def yanxi_thread(self):
        self.yanxiList_ = WorkThread(timer=self.yanxi_timer.value())
        self.yanxiList_.moveToThread(self.yanxiThread)
        self.yanxiThread.started.connect(self.yanxiList_.yan_xi)
        self.yanxiThread.start()



if __name__ == "__main__":
    b = BiLanHangXian()
    app = QApplication()
    myWin = MyMainWindow()
    myWin.show()
    app.exec()