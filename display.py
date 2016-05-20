#################
import sys
from PyQt5.QtWidgets import QWidget, QApplication,QFrame
from PyQt5.QtGui import QPainter, QColor, QBrush, QImage

#################


from PyQt5 import QtGui, QtCore
from components import Object


class Bitmap(QWidget):
    def __init__(self, bitmapData):
        super(Bitmap, self).__init__()

        self.bitmapData = bitmapData
        self.bitmapImg = self.bitmapData.image
        self.imgToPrint

    def _getOriginalWidth(self):
        return self.bitmapData.width

    def _getOriginalHeight(self):
        return self.bitmapData.height

    def _loopDraw(self, c):
        if isinstance(self.bitmapImg, QtGui.QPixmap):
            c.drawPixmap(0, 0, self.bitmapImg, self.bitmapData.x, self.bitmapData.y, self.bitmapData.width,
                         self.bitmapData.height)
        elif isinstance(self.bitmapImg, QtGui.QImage):
            c.drawImage(0, 0, self.bitmapImg, self.bitmapData.x, self.bitmapData.y, self.bitmapData.width,
                        self.bitmapData.height)


# good
class BitmapData(Object):
    def __init__(self, img=QtGui.QImage(), x=0, y=0, width=0, height=0):
        super(BitmapData, self).__init__()

        if isinstance(img, QtGui.QImage):
            img = QtGui.QPixmap(img)

        elif not isinstance(img, QtGui.QPixmap):
            raise TypeError(" parameter 'image' must be a QPixmap or QImage object.")

        self.image = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.__locked = False
        # self.__pixelData = []

        if img is not None:

            if width == 0:
                self.width = img.width()

            if height == 0:
                self.height = img.height()

    def setCoordinate(self, x=0, y=0):
        self.x = x
        self.y = y

    def setProperties(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Example(QFrame):
    def __init__(self):
        super().__init__()

        # self.imgToPrint = self.openImage("assets/t.png")
        self.imgToPrint = QImage("assets/t.png")
        self.imgToPrint2 = self.openImage("assets/coliseum.jpg")

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, event):

        # painter = QtGui.QPainter(self)
        # painter.begin(self.image1)
        # painter.drawImage(0, 0, self.image1)
        # painter.drawImage(50, 0, self.image2)
        # painter.end()

        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.imgToPrint2, 0, 0, -1, -1)
        # painter.translate(20, 20)
        painter.scale(3, 3)
        painter.rotate(15)
        painter.drawImage(0, 0, self.imgToPrint, 0, 0, -1, -1)

    def openImage(self, fileName):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return None
        self.modified = False
        self.update()
        return loadedImage


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
