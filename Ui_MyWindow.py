# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_MyWindow(object):
    def setupUi(self, MyWindow):
        if not MyWindow.objectName():
            MyWindow.setObjectName(u"MyWindow")
        MyWindow.resize(400, 300)
        self.layoutWidget = QWidget(MyWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 130, 191, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.yanxi_timer = QSpinBox(self.layoutWidget)
        self.yanxi_timer.setObjectName(u"yanxi_timer")
        self.yanxi_timer.setMaximum(10)
        self.yanxi_timer.setValue(10)

        self.horizontalLayout.addWidget(self.yanxi_timer)

        self.yanxi_button = QPushButton(self.layoutWidget)
        self.yanxi_button.setObjectName(u"yanxi_button")

        self.horizontalLayout.addWidget(self.yanxi_button)


        self.retranslateUi(MyWindow)

        QMetaObject.connectSlotsByName(MyWindow)
    # setupUi

    def retranslateUi(self, MyWindow):
        MyWindow.setWindowTitle(QCoreApplication.translate("MyWindow", u"\u78a7\u84dd\u822a\u7ebf", None))
        self.label.setText(QCoreApplication.translate("MyWindow", u"\u6f14\u4e60", None))
        self.yanxi_button.setText(QCoreApplication.translate("MyWindow", u"PushButton", None))
    # retranslateUi

