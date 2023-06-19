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
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_MyWindow(object):
    def setupUi(self, MyWindow):
        if not MyWindow.objectName():
            MyWindow.setObjectName(u"MyWindow")
        MyWindow.setEnabled(True)
        MyWindow.resize(201, 186)
        MyWindow.setAcceptDrops(False)
        self.verticalLayout_2 = QVBoxLayout(MyWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(MyWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setAcceptDrops(False)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(MyWindow)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setAcceptDrops(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.yanxi_timer = QSpinBox(MyWindow)
        self.yanxi_timer.setObjectName(u"yanxi_timer")
        self.yanxi_timer.setMinimumSize(QSize(60, 0))
        self.yanxi_timer.setMaximumSize(QSize(60, 16777215))
        self.yanxi_timer.setAcceptDrops(False)
        self.yanxi_timer.setMaximum(10)
        self.yanxi_timer.setValue(10)

        self.horizontalLayout.addWidget(self.yanxi_timer)

        self.yanxi_button_0 = QPushButton(MyWindow)
        self.yanxi_button_0.setObjectName(u"yanxi_button_0")
        self.yanxi_button_0.setMaximumSize(QSize(40, 30))
        self.yanxi_button_0.setAcceptDrops(False)

        self.horizontalLayout.addWidget(self.yanxi_button_0)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(MyWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))
        self.label_4.setAcceptDrops(False)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.yanxi_timer_4 = QSpinBox(MyWindow)
        self.yanxi_timer_4.setObjectName(u"yanxi_timer_4")
        self.yanxi_timer_4.setEnabled(True)
        self.yanxi_timer_4.setMinimumSize(QSize(60, 0))
        self.yanxi_timer_4.setMaximumSize(QSize(60, 16777215))
        self.yanxi_timer_4.setAcceptDrops(False)
        self.yanxi_timer_4.setMaximum(10)
        self.yanxi_timer_4.setValue(10)

        self.horizontalLayout_4.addWidget(self.yanxi_timer_4)

        self.yanxi_button_1 = QPushButton(MyWindow)
        self.yanxi_button_1.setObjectName(u"yanxi_button_1")
        self.yanxi_button_1.setEnabled(True)
        self.yanxi_button_1.setMinimumSize(QSize(10, 10))
        self.yanxi_button_1.setMaximumSize(QSize(40, 30))
        self.yanxi_button_1.setAcceptDrops(False)

        self.horizontalLayout_4.addWidget(self.yanxi_button_1)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(MyWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))
        self.label_3.setAcceptDrops(False)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.yanxi_timer_3 = QSpinBox(MyWindow)
        self.yanxi_timer_3.setObjectName(u"yanxi_timer_3")
        self.yanxi_timer_3.setMinimumSize(QSize(60, 0))
        self.yanxi_timer_3.setMaximumSize(QSize(60, 16777215))
        self.yanxi_timer_3.setAcceptDrops(False)
        self.yanxi_timer_3.setMaximum(10)
        self.yanxi_timer_3.setValue(10)

        self.horizontalLayout_3.addWidget(self.yanxi_timer_3)

        self.yanxi_button_2 = QPushButton(MyWindow)
        self.yanxi_button_2.setObjectName(u"yanxi_button_2")
        self.yanxi_button_2.setMaximumSize(QSize(40, 30))
        self.yanxi_button_2.setAcceptDrops(False)

        self.horizontalLayout_3.addWidget(self.yanxi_button_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(MyWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))
        self.label_2.setAcceptDrops(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.yanxi_timer_2 = QSpinBox(MyWindow)
        self.yanxi_timer_2.setObjectName(u"yanxi_timer_2")
        self.yanxi_timer_2.setMinimumSize(QSize(60, 0))
        self.yanxi_timer_2.setMaximumSize(QSize(60, 16777215))
        self.yanxi_timer_2.setAcceptDrops(False)
        self.yanxi_timer_2.setMaximum(10)
        self.yanxi_timer_2.setValue(10)

        self.horizontalLayout_2.addWidget(self.yanxi_timer_2)

        self.yanxi_button_4 = QPushButton(MyWindow)
        self.yanxi_button_4.setObjectName(u"yanxi_button_4")
        self.yanxi_button_4.setMaximumSize(QSize(40, 30))
        self.yanxi_button_4.setAcceptDrops(False)

        self.horizontalLayout_2.addWidget(self.yanxi_button_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(MyWindow)

        QMetaObject.connectSlotsByName(MyWindow)
    # setupUi

    def retranslateUi(self, MyWindow):
        MyWindow.setWindowTitle(QCoreApplication.translate("MyWindow", u"\u78a7\u84dd\u822a\u7ebf", None))
        self.label_5.setText(QCoreApplication.translate("MyWindow", u"\u6797\u80af\u6b7b\u5927\u5934", None))
        self.label.setText(QCoreApplication.translate("MyWindow", u"\u6f14\u4e60", None))
        self.yanxi_button_0.setText(QCoreApplication.translate("MyWindow", u"\u5f00\u59cb", None))
        self.label_4.setText(QCoreApplication.translate("MyWindow", u"\u6f14\u4e60", None))
        self.yanxi_button_1.setText(QCoreApplication.translate("MyWindow", u"\u5f00\u59cb", None))
        self.label_3.setText(QCoreApplication.translate("MyWindow", u"\u6f14\u4e60", None))
        self.yanxi_button_2.setText(QCoreApplication.translate("MyWindow", u"\u5f00\u59cb", None))
        self.label_2.setText(QCoreApplication.translate("MyWindow", u"\u6f14\u4e60", None))
        self.yanxi_button_4.setText(QCoreApplication.translate("MyWindow", u"\u5f00\u59cb", None))
    # retranslateUi

