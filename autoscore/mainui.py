# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

from filelistwidget import FileListWidget

class Ui_MainWindowAutoScore(object):
    def setupUi(self, MainWindowAutoScore):
        if not MainWindowAutoScore.objectName():
            MainWindowAutoScore.setObjectName(u"MainWindowAutoScore")
        MainWindowAutoScore.resize(900, 645)
        MainWindowAutoScore.setMinimumSize(QSize(900, 645))
        MainWindowAutoScore.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)
        MainWindowAutoScore.setFont(font)
        MainWindowAutoScore.setAcceptDrops(True)
        self.centralwidget = QWidget(MainWindowAutoScore)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayoutFull = QVBoxLayout()
        self.verticalLayoutFull.setObjectName(u"verticalLayoutFull")
        self.verticalLayoutFull.setContentsMargins(10, 10, 10, 10)
        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setMinimumSize(QSize(0, 150))
        self.labelTitle.setMaximumSize(QSize(16777215, 16777215))
        self.labelTitle.setAcceptDrops(False)

        self.verticalLayoutFull.addWidget(self.labelTitle)

        self.listWidgetFileList = FileListWidget(self.centralwidget)
        self.listWidgetFileList.setObjectName(u"listWidgetFileList")
        self.listWidgetFileList.setMinimumSize(QSize(0, 215))
        self.listWidgetFileList.setFont(font)
        self.listWidgetFileList.setAcceptDrops(True)
        self.listWidgetFileList.setDragEnabled(False)
        self.listWidgetFileList.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.listWidgetFileList.setAlternatingRowColors(True)

        self.verticalLayoutFull.addWidget(self.listWidgetFileList)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelAdjustments = QLabel(self.centralwidget)
        self.labelAdjustments.setObjectName(u"labelAdjustments")
        self.labelAdjustments.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.labelAdjustments)

        self.lineEditAdjustments = QLineEdit(self.centralwidget)
        self.lineEditAdjustments.setObjectName(u"lineEditAdjustments")

        self.horizontalLayout_2.addWidget(self.lineEditAdjustments)


        self.verticalLayoutFull.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.spinboxScoresToDrop = QSpinBox(self.centralwidget)
        self.spinboxScoresToDrop.setObjectName(u"spinboxScoresToDrop")
        self.spinboxScoresToDrop.setMaximum(10)

        self.horizontalLayout_3.addWidget(self.spinboxScoresToDrop)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayoutFull.addLayout(self.horizontalLayout_3)

        self.checkBoxAppendToFile = QCheckBox(self.centralwidget)
        self.checkBoxAppendToFile.setObjectName(u"checkBoxAppendToFile")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxAppendToFile.sizePolicy().hasHeightForWidth())
        self.checkBoxAppendToFile.setSizePolicy(sizePolicy)

        self.verticalLayoutFull.addWidget(self.checkBoxAppendToFile)

        self.checkBoxEndAfterProcess = QCheckBox(self.centralwidget)
        self.checkBoxEndAfterProcess.setObjectName(u"checkBoxEndAfterProcess")
        self.checkBoxEndAfterProcess.setChecked(True)

        self.verticalLayoutFull.addWidget(self.checkBoxEndAfterProcess)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonProcess = QPushButton(self.centralwidget)
        self.pushButtonProcess.setObjectName(u"pushButtonProcess")
        self.pushButtonProcess.setEnabled(False)
        self.pushButtonProcess.setMinimumSize(QSize(0, 41))
        self.pushButtonProcess.setMaximumSize(QSize(16777215, 41))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.pushButtonProcess.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButtonProcess)

        self.pushButtonClearList = QPushButton(self.centralwidget)
        self.pushButtonClearList.setObjectName(u"pushButtonClearList")
        self.pushButtonClearList.setEnabled(False)
        self.pushButtonClearList.setMinimumSize(QSize(100, 41))
        self.pushButtonClearList.setMaximumSize(QSize(200, 41))
        self.pushButtonClearList.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButtonClearList)

        self.pushButtonQuit = QPushButton(self.centralwidget)
        self.pushButtonQuit.setObjectName(u"pushButtonQuit")
        self.pushButtonQuit.setMinimumSize(QSize(100, 41))
        self.pushButtonQuit.setMaximumSize(QSize(150, 41))
        self.pushButtonQuit.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButtonQuit)


        self.verticalLayoutFull.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayoutFull, 0, 0, 1, 1)

        MainWindowAutoScore.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowAutoScore)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowAutoScore.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowAutoScore)

        QMetaObject.connectSlotsByName(MainWindowAutoScore)
    # setupUi

    def retranslateUi(self, MainWindowAutoScore):
        MainWindowAutoScore.setWindowTitle(QCoreApplication.translate("MainWindowAutoScore", u"AutoScore Files", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindowAutoScore", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">AutoScore Files v4.4.0</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Travis L. Seymour, PhD</span></p><hr/><p>Drag/Drop Files or Folders here (.txt and .docx only)</p></body></html>", None))
        self.labelAdjustments.setText(QCoreApplication.translate("MainWindowAutoScore", u"Global Adjustment(s):", None))
#if QT_CONFIG(tooltip)
        self.lineEditAdjustments.setToolTip(QCoreApplication.translate("MainWindowAutoScore", u"<html><head/><body><p>adjustment, message, min eligible meanAdj, max eligible meanAdj<br/>{10|Overall adjustment for coarseness of rubric|1|99}<br/>{-5|Penalty for 1-page over page limit}<br/>Note: Can either be here or in paper. E.g.,<br/>overall adjustments could go here, but individual<br/>student adjustment could go in their papers.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindowAutoScore", u"Drop The Lowest", None))
        self.label_2.setText(QCoreApplication.translate("MainWindowAutoScore", u"Scores", None))
        self.checkBoxAppendToFile.setText(QCoreApplication.translate("MainWindowAutoScore", u"Append Socre Information to End of File?", None))
        self.checkBoxEndAfterProcess.setText(QCoreApplication.translate("MainWindowAutoScore", u"Close App After Process Completes?", None))
        self.pushButtonProcess.setText(QCoreApplication.translate("MainWindowAutoScore", u"PROCESS FILE(S)", None))
        self.pushButtonClearList.setText(QCoreApplication.translate("MainWindowAutoScore", u"Clear List", None))
        self.pushButtonQuit.setText(QCoreApplication.translate("MainWindowAutoScore", u"QUIT", None))
    # retranslateUi

