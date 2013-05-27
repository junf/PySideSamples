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


def fadein(target, duration) -> 'Animation object':
    """Get animation to fade in the image
    :param target: Target property of animation(QGraphicsOpacityEffect)
    :param duration: Time spent on animation
    """
    an = QtCore.QPropertyAnimation(target, "opacity")
    an.setDuration(duration)
    an.setStartValue(0)
    an.setEndValue(1)
    return an

def fadeout(target, duration) -> 'Animation object':
    """Get animation to fade out the image
    :param target: Target property of animation
    :param duration: Time spent on animation
    """
    an = QtCore.QPropertyAnimation(target, "opacity")
    an.setDuration(duration)
    an.setStartValue(1)
    an.setEndValue(0)
    return an

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # Label to show backgroud image('huga.jpg')
    blabel = QtGui.QLabel()
    bmap = QtGui.QPixmap('fuga.jpg')
    blabel.setPixmap(bmap)
    blabel.resize(bmap.size())
    blabel.show()

    # Label to show foreground image('hoge.jpg')
    flabel = QtGui.QLabel(blabel)
    fmap = QtGui.QPixmap('hoge.jpg')
    flabel.setPixmap(fmap)
    flabel.resize(fmap.size())
    flabel.show()

    # Put opacity effect to front label
    effect = QtGui.QGraphicsOpacityEffect()
    effect.setOpacity(0.5)
    flabel.setGraphicsEffect(effect)

    # Configure and run the animation
    ag = QtCore.QSequentialAnimationGroup()
    ag.addAnimation(fadein(effect, 2000))
    ag.addPause(2000)
    ag.addAnimation(fadeout(effect, 2000))
    ag.start()

    sys.exit(app.exec_())
