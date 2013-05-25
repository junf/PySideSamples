"""
   Copyright 2013 Jun Funada

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import sys
from PySide import QtCore
from PySide import QtGui

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()

    label = QtGui.QLabel(window)
    pixmap = QtGui.QPixmap('hoge.jpg')
    label.setPixmap(pixmap)
    label.resize(pixmap.size())

    window.setGeometry(100, 100, 900, 700)
    window.show()

    an = QtCore.QPropertyAnimation(label, 'pos')
    an.setDuration(10000)
    an.setStartValue(QtCore.QPoint(800, 600))
    an.setEndValue(QtCore.QPoint(0, 0))
    an.start()

    sys.exit(app.exec_())
