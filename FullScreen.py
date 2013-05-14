import sys
from PySide import QtCore
from PySide import QtGui

app = QtGui.QApplication(sys.argv)
pixmap = QtGui.QPixmap('hoge.jpg')
window = QtGui.QLabel()
window.setPixmap(pixmap)
window.show()
sys.exit(app.exec_())
