import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
from Ui_untitled import Ui_Dialog


class MyMainWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # MainWindow = QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())