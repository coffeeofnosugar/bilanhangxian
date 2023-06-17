import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from Ui_MainWindow import Ui_MainWindow
from win32 import BiLanHangXian


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.b = BiLanHangXian()
        self.band()
    

    def band(self):
        self.yanxi_button.clicked.connect(lambda : self.b.yan_xi(self.yanxi_timer.value()))
        self.yanxi_timer.value()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())