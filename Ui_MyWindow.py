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
        MyWindow.resize(259, 233)
        MyWindow.setAcceptDrops(False)
        self.verticalLayout = QVBoxLayout(MyWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(MyWindow)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setEnabled(True)
        self.label_title.setMinimumSize(QSize(0, 0))
        self.label_title.setMaximumSize(QSize(16777215, 50))
        self.label_title.setAcceptDrops(False)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_0 = QLabel(MyWindow)
        self.label_0.setObjectName(u"label_0")
        self.label_0.setMinimumSize(QSize(50, 0))
        self.label_0.setMaximumSize(QSize(100, 16777215))
        self.label_0.setAcceptDrops(False)
        self.label_0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_0)

        self.yanxi_timer = QSpinBox(MyWindow)
        self.yanxi_timer.setObjectName(u"yanxi_timer")
        self.yanxi_timer.setMinimumSize(QSize(70, 0))
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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_1 = QLabel(MyWindow)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(50, 0))
        self.label_1.setMaximumSize(QSize(100, 16777215))
        self.label_1.setAcceptDrops(False)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_1)

        self.meishi_timer = QSpinBox(MyWindow)
        self.meishi_timer.setObjectName(u"meishi_timer")
        self.meishi_timer.setEnabled(False)
        self.meishi_timer.setMinimumSize(QSize(70, 0))
        self.meishi_timer.setMaximumSize(QSize(60, 16777215))
        self.meishi_timer.setAcceptDrops(False)
        self.meishi_timer.setMaximum(10)
        self.meishi_timer.setValue(10)

        self.horizontalLayout_2.addWidget(self.meishi_timer)

        self.meishi_button_1 = QPushButton(MyWindow)
        self.meishi_button_1.setObjectName(u"meishi_button_1")
        self.meishi_button_1.setMaximumSize(QSize(40, 30))
        self.meishi_button_1.setAcceptDrops(False)

        self.horizontalLayout_2.addWidget(self.meishi_button_1)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(MyWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))
        self.label_2.setAcceptDrops(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.jichuxunhuan_timer_2 = QSpinBox(MyWindow)
        self.jichuxunhuan_timer_2.setObjectName(u"jichuxunhuan_timer_2")
        self.jichuxunhuan_timer_2.setMinimumSize(QSize(70, 0))
        self.jichuxunhuan_timer_2.setMaximumSize(QSize(60, 16777215))
        self.jichuxunhuan_timer_2.setAcceptDrops(False)
        self.jichuxunhuan_timer_2.setMaximum(99)
        self.jichuxunhuan_timer_2.setValue(1)

        self.horizontalLayout_3.addWidget(self.jichuxunhuan_timer_2)

        self.jichuxunhuan_button_2 = QPushButton(MyWindow)
        self.jichuxunhuan_button_2.setObjectName(u"jichuxunhuan_button_2")
        self.jichuxunhuan_button_2.setMaximumSize(QSize(40, 30))
        self.jichuxunhuan_button_2.setAcceptDrops(False)

        self.horizontalLayout_3.addWidget(self.jichuxunhuan_button_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stop_button_3 = QPushButton(MyWindow)
        self.stop_button_3.setObjectName(u"stop_button_3")
        self.stop_button_3.setEnabled(True)
        self.stop_button_3.setMinimumSize(QSize(10, 10))
        self.stop_button_3.setMaximumSize(QSize(200, 30))
        self.stop_button_3.setAcceptDrops(False)

        self.horizontalLayout_4.addWidget(self.stop_button_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(MyWindow)

        QMetaObject.connectSlotsByName(MyWindow)
    # setupUi

    def retranslateUi(self, MyWindow):
        MyWindow.setWindowTitle(QCoreApplication.translate("MyWindow", u"\u78a7\u84dd\u822a\u7ebf", None))
        self.label_title.setText(QCoreApplication.translate("MyWindow", u"\u6797\u80af\u6b7b\u5927\u5934", None))
        self.label_0.setText(QCoreApplication.translate("MyWindow", u"\u6f14\u4e60", None))
        self.yanxi_button_0.setText(QCoreApplication.translate("MyWindow", u"\u5f00\u59cb", None))
        self.label_1.setText(QCoreApplication.translate("MyWindow", u"\u796d\u5178\u7f8e\u98df", None))
        self.meishi_button_1.setText(QCoreApplication.translate("MyWindow", u"\u5f00\u59cb", None))
        self.label_2.setText(QCoreApplication.translate("MyWindow", u"\u57fa\u7840\u5faa\u73af", None))
        self.jichuxunhuan_button_2.setText(QCoreApplication.translate("MyWindow", u"\u5f00\u59cb", None))
        self.stop_button_3.setText(QCoreApplication.translate("MyWindow", u"\u7ed3\u675f\u5f53\u524d\u8fdb\u7a0b", None))
    # retranslateUi

