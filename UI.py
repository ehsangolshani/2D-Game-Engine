# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QFrame
from PyQt5.QtGui import QPainter, QColor, QBrush, QImage
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView
from PyQt5.QtCore import pyqtSignal, QObject

from components import Object, Sprite


class Communicate(QObject):
    # get the file path and type name of the selected img
    spriteDrawMsg = pyqtSignal(str, str)

    # get the type name of the selected rect
    rectDrawMsg = pyqtSignal(str)

    # get the type name of the selected rect
    circleDrawMsg = pyqtSignal(str)


class E(QFrame):
    def __init__(self, x):
        super().__init__(x)

        self.sprites = []

    def spriteDrawController(self, assetAddress, drawType):
        if drawType == "sprite":
            self.sprites.append(Sprite(QImage(assetAddress)))
            self.update()

        elif drawType == "sprite type 2":
            print("draw sprite type 2")
        else:
            print("draw other sprite")

    def rectDrawController(self, drawType):
        if drawType == "rect":
            print("main part")

        elif drawType == "rect type 2":
            print("draw rect type 2")
        else:
            print("draw other rect")

    def circleDrawController(self, drawType):
        if drawType == "circle":
            print("main part")

        elif drawType == "circle type 2":
            print("draw circle type 2")
        else:
            print("draw other circle")

    def paintEvent(self, event):

        if self.sprites is not []:
            painter = QtGui.QPainter(self)
            for s in self.sprites:
                if s is not None:
                    painter.scale(s.scaleX, s.scaleY)
                    painter.rotate(s.rotation)
                    painter.drawImage(s.x, s.y, QtGui.QImage(s.image), 0, 0, -1, -1)

    def openImage(self, fileName):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return None
        self.modified = False
        self.update()
        self.imgToPrint = loadedImage
        return loadedImage


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 482)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.frame = E(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 431, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.c = Communicate()
        self.c.spriteDrawMsg.connect(self.frame.spriteDrawController)
        self.c.rectDrawMsg.connect(self.frame.rectDrawController)
        self.c.circleDrawMsg.connect(self.frame.circleDrawController)

        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(450, 10, 221, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.treeView = QtWidgets.QTreeView(self.tab_2)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 221, 221))
        self.treeView.setObjectName("treeView")

        ########################################### get selected sprite file path and send signal to frame

        def sendSpriteDrawMsg(item):
            index = self.treeView.currentIndex()
            p = self.model.filePath(index)

            self.c.spriteDrawMsg.emit(p, "sprite")

        self.treeView.doubleClicked.connect(sendSpriteDrawMsg)

        ##################################################################################################



        ########################################### send drawRect signal to frame

        def sendRectDrawMsg(item):
            # do needed things here

            self.c.spriteDrawMsg.emit("rect")

        # send a signal to sendRectDrawMsg here

        ##########################################################################



        ########################################### send drawCircle signal to frame

        def sendCircleDrawMsg(item):
            # do needed things here

            self.c.spriteDrawMsg.emit("circle")

        # send a signal to sendCircleDrawMsg here

        #############################################################################

        self.model = QFileSystemModel()
        self.path = "."
        self.model.setRootPath(self.path)

        # self.filter = Iterable("*.png")
        # self.model.setNameFilters(self.filter)

        # self.model.removeColumn(1)
        # self.model.removeColumn(2)
        # self.model.removeColumn(3)
        # self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot | QDir.AllEntries)
        #
        # self.proxyModel = QSortFilterProxyModel()
        # self.proxyModel.setSourceModel(model)
        # self.proxyModel.removeColumn(1)
        # self.proxyModel.removeColumn(2)
        # self.proxyModel.removeColumn(3)

        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(self.path))
        self.treeView.expandAll()

        self.listView = QtWidgets.QListView(self.tab_2)
        self.listView.setGeometry(QtCore.QRect(0, 240, 221, 141))
        self.listView.setObjectName("listView")

        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(30, 220, 151, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 680, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuChert_Engine = QtWidgets.QMenu(self.menuBar)
        self.menuChert_Engine.setObjectName("menuChert_Engine")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuChert_Engine.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuChert_Engine.setTitle(_translate("MainWindow", "Chert Engine"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
