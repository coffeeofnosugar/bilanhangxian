import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from Ui_MyWindow import Ui_MyWindow
from win32 import BiLanHangXian, GetImage


class MyMainWindow(Ui_MyWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.band()
    

    def band(self):
        # self.yanxi_button.clicked.connect(lambda : self.b.yan_xi(self.yanxi_timer.value()))
        self.yanxi_button.clicked.connect(lambda : b.FindTarget(GetImage(".\\image\\test_1.png")))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    b = BiLanHangXian()
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())