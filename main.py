from win32 import BiLanHangXian, GetImage
from PySide6.QtWidgets import QApplication, QWidget
from Ui_MyWindow import Ui_MyWindow
from PySide6.QtCore import QObject, QThread, Signal
import time
import ctypes

# 用于获取线程 ID 的函数
def get_thread_id(thread):
    handle = thread.currentThread()
    if handle:
        return int(handle)
    return None

# 用于强制终止线程的函数
def terminate_thread(thread_id):
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.OpenThread(1, False, thread_id)
    kernel32.TerminateThread(handle, -1)
    kernel32.CloseHandle(handle)


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
    
    @Exit
    def ji_chu_xun_huan(self):
        print('jichuxunhuan start')
        b.ji_chu_xun_huan(self.kwargs['timer'])
        

    

class MyMainWindow(Ui_MyWindow, QWidget):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.bind()

        
    def bind(self):
        # yan_xi
        self.yanxi_thread = QThread()
        self.yanxi_thread.finished.connect(self.finished)
        self.yanxi_button_0.clicked.connect(self.yan_xi)


        # ji_dian_mei_shi
        self.meishi_thread = QThread()
        self.meishi_thread.finished.connect(self.finished)
        self.meishi_button_1.clicked.connect(self.ji_dian_mei_shi)

        #ji_chu_xun_huan
        self.xunhuan_thread = QThread()
        self.xunhuan_thread.finished.connect(self.finished)
        self.jichuxunhuan_button_2.clicked.connect(self.ji_chu_xun_huan)

        # stop
        self.stop_button_3.clicked.connect(self.stop)

        
    def yan_xi(self):
        self.yanxi_button_0.setEnabled(False)
        self.meishi_button_1.setEnabled(False)
        self.jichuxunhuan_button_2.setEnabled(False)
        self.yanxiList = WorkThread(timer=self.yanxi_timer.value())
        self.yanxiList.moveToThread(self.yanxi_thread)
        self.yanxi_thread.started.connect(self.yanxiList.yan_xi)
        self.yanxi_thread.start()
    
    def ji_dian_mei_shi(self):
        self.yanxi_button_0.setEnabled(False)
        self.meishi_button_1.setEnabled(False)
        self.jichuxunhuan_button_2.setEnabled(False)
        self.meishiList = WorkThread()
        self.meishiList.moveToThread(self.meishi_thread)
        self.meishi_thread.started.connect(self.meishiList.ji_dian_mei_shi)
        self.meishi_thread.start()

    def ji_chu_xun_huan(self):
        self.yanxi_button_0.setEnabled(False)
        self.meishi_button_1.setEnabled(False)
        self.jichuxunhuan_button_2.setEnabled(False)
        self.xunhuanList = WorkThread(timer=self.jichuxunhuan_timer_2.value())
        self.xunhuanList.moveToThread(self.xunhuan_thread)
        self.xunhuan_thread.started.connect(self.xunhuanList.ji_chu_xun_huan)
        self.xunhuan_thread.start()

    def finished(self):
        print('finished')
        self.yanxi_button_0.setEnabled(True)
        self.meishi_button_1.setEnabled(True)
        self.jichuxunhuan_button_2.setEnabled(True)

    def stop(self):
        print(123)
        # self.yanxi_thread.terminate()
        # # self.yanxi_thread.quit()
        # print(self.yanxi_thread.isFinished())
        terminate_thread(get_thread_id(self.yanxiList))
        


if __name__ == "__main__":
    print("main.py    ", __name__)
    b = BiLanHangXian()
    app = QApplication()
    myWin = MyMainWindow()
    myWin.show()
    app.exec()