from PyQt5 import QtGui


class Object(object):
    def __init__(self, n='', x=0, y=0, sx=1, sy=1, r=0, p=0):
        self.name = n
        self.x = x
        self.y = y
        self.scaleX = sx
        self.scaleY = sy
        self.rotation = r
        self.width = 0
        self.height = 0
        self.priority = p
        self.backgroundcolor = None
        self.childList = []

    def startX(self):
        return self.x

    def startY(self):
        return self.y

    def endX(self):
        return self.x + self.width

    def endY(self):
        return self.y + self.height


class Sprite(Object):
    def __init__(self, img):
        super(Sprite, self).__init__()

        if (img is not None) and isinstance(img, QtGui.QImage):
            self.image = img
        else:
            self.image = QtGui.QImage

        self.pixmap = QtGui.QPixmap

# def _setCanvas(self, speed, title, width, height):
#     self.speed = speed
#     self.width = width
#     self.height = height
#
#     self.canvas = QtGui.QPainter()
#
#     self.canvasWidget = CanvasWidget()
#     self.canvasWidget.setWindowTitle(title)
#     self.canvasWidget.setFixedSize(width, height)
#     self.canvasWidget.show()
#
#     self.timer = QtCore.QTimer()
#     self.timer.setInterval(speed)
#     self.timer.start();
#
#     QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.canvasWidget, QtCore.SLOT("update()"))
