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


def zoom(target, duration, mag1, mag2) -> 'Animation object':
    """Return the animation to display target widget while zoom (pin left upper corner)
    :param target: target widget
    :param duration: time spent by the animation
    :param mag1: initial magnification of zoom
    :param mag2: final magnification of zoom
    """

    target.setScaledContents(True)

    animation = QtCore.QPropertyAnimation(target, "size")
    animation.setDuration(duration)

    mapsize = target.pixmap().size()
    animation.setStartValue(mapsize * mag1)
    animation.setEndValue(mapsize * mag2)

    return animation


def zoom2(target, duration, mag1, mag2):
    """Return the animation to display target widget while zoom (pin target center)
    :param target: target widget
    :param duration: time spent by the animation
    :param mag1: initial magnification of zoom
    :param mag2: final magnification of zoom
    """

    ang = QtCore.QParallelAnimationGroup()

    # add zoom animation
    an_zoom = zoom(target, duration, mag1, mag2)
    ang.addAnimation(an_zoom)

    # add move animation
    pos1 = posZoomed(target, mag1)
    pos2 = posZoomed(target, mag2)
    an_pos = move(target, duration, pos1, pos2)
    ang.addAnimation(an_pos)

    return ang


def move(target, duration, pos1, pos2) -> 'Animation object':
    """Return the animation to move target widget
    :param target: target widget
    :param duration: time spent by the animation
    :param pos1: initial position at left upper conrer (QPoint)
    :param pos2: final position at left upper conrer (QPoint)
    """
    animation = QtCore.QPropertyAnimation(target, "pos")
    animation.setDuration(duration)
    animation.setStartValue(pos1)
    animation.setEndValue(pos2)

    return animation


def posOnParentCenter(parent, width, height) -> 'pos (QPoint)':
    """Return the pos when placed at the center to the parent widget
    :param parent: parent widget
    :param width: width
    :param height: height
    """
    c = parent.rect().center()
    return QtCore.QPoint(c.x() - width / 2, c.y() - height / 2)


def posZoomed(target, mag) -> 'pos (QPoint)':
    """Return the pos when zoomed
    Return 'pos' property when zoomed by the magnification 'mag' while pin the center
    :param target: target to be zoomed
    :param mag: magnification
    """
    g = target.geometry()
    c = g.center()
    return QtCore.QPoint(c.x() - g.width() / 2 * mag, c.y() - g.height() / 2 * mag)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()

    label = QtGui.QLabel(window)
    pixmap = QtGui.QPixmap('hoge.jpg')
    label.setPixmap(pixmap)
    label.resize(pixmap.size())

    window.setGeometry(100, 100, 900, 700)
    window.show()
#    an = zoom(label, 10000, 1, 2)
    label.move(posOnParentCenter(window, label.width(), label.height()))
    an = zoom2(label, 10000, 1, 2)
    an.start()

    sys.exit(app.exec_())
