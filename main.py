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
    
    @Exit
    def ji_dian_mei_shi(self):
        print("meishi start")
        b.ji_dian_mei_shi()
        

    

class MyMainWindow(Ui_MyWindow, QWidget):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.bind()

        
    def bind(self):
        # yan_xi
        self.yanxi_thread = QThread()
        self.yanxi_thread.finished.connect(lambda: print('yan_xi finished'))
        self.yanxi_button_0.clicked.connect(self.yan_xi)


        # meishijidian
        self.meishi_thread = QThread()
        self.meishi_thread.finished.connect(lambda: print('meishijidian finished'))
        self.meishi_button_1.clicked.connect(self.ji_dian_mei_shi)
        
    def yan_xi(self):
        self.yanxiList = WorkThread(timer=self.yanxi_timer.value())
        self.yanxiList.moveToThread(self.yanxi_thread)
        self.yanxi_thread.started.connect(self.yanxiList.yan_xi)
        self.yanxi_thread.start()
    
    def ji_dian_mei_shi(self):
        self.meishiList = WorkThread()
        self.meishiList.moveToThread(self.meishi_thread)
        self.meishi_thread.started.connect(self.meishiList.ji_dian_mei_shi)
        self.meishi_thread.start()



if __name__ == "__main__":
    b = BiLanHangXian()
    app = QApplication()
    myWin = MyMainWindow()
    myWin.show()
    app.exec()