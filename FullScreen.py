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
