import sys
from PySide import QtCore
from PySide import QtGui


class Screen(QtGui.QLabel):
    def __init__(self, parent=None, f=0):
        QtGui.QLabel.__init__(self, parent, f)

    def keyPressEvent(self, event):
        QtGui.QLabel.keyPressEvent(self, event)
        if event.key() == QtCore.Qt.Key_Escape:
            print(event.key())
            if self.isFullScreen():
                self.showNormal()
                self.showMaximized()
            else:
                self.showFullScreen()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    pixmap = QtGui.QPixmap('hoge.jpg')
    screen = Screen()
    screen.setPixmap(pixmap)
    screen.showFullScreen()
    sys.exit(app.exec_())
