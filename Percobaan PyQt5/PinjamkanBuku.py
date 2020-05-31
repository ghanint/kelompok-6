# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PinjamkanBuku.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LendWindow(object):
    def setupUi(self, LendWindow):
        LendWindow.setObjectName("LendWindow")
        LendWindow.resize(800, 529)
        self.centralwidget = QtWidgets.QWidget(LendWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 90, 731, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 30, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(580, 450, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        LendWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LendWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        LendWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LendWindow)
        self.statusbar.setObjectName("statusbar")
        LendWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LendWindow)
        QtCore.QMetaObject.connectSlotsByName(LendWindow)

    def retranslateUi(self, LendWindow):
        _translate = QtCore.QCoreApplication.translate
        LendWindow.setWindowTitle(_translate("LendWindow", "Pinjamkan Buku"))
        self.comboBox.setItemText(0, _translate("LendWindow", "Al-Quran"))
        self.comboBox.setItemText(1, _translate("LendWindow", "Al-Kitab"))
        self.comboBox.setItemText(2, _translate("LendWindow", "Weda"))
        self.comboBox.setItemText(3, _translate("LendWindow", "Tripitaka"))
        self.comboBox.setItemText(4, _translate("LendWindow", "Shishu Wujing"))
        self.label.setText(_translate("LendWindow", "Pilih Buku yang ingin dipinjam"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LendWindow = QtWidgets.QMainWindow()
    ui = Ui_LendWindow()
    ui.setupUi(LendWindow)
    LendWindow.show()
    sys.exit(app.exec_())
