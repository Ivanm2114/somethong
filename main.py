import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.pushButton = QPushButton(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Вторая программа')

        self.pushButton.setText('Press Me')
        self.pushButton.resize(100, 50)
        self.pushButton.move(200, 200)
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawRectangles(qp)
            qp.end()

    def drawRectangles(self, qp):
        qp.setBrush(QColor(randint(0, 255),
                           randint(0, 255),
                           randint(0, 255)))
        size = randint(1, 3)
        qp.drawEllipse(10, 15, 20 * size, 20 * size)
        size = randint(1, 3)
        qp.setBrush(QColor(randint(0, 255),
                           randint(0, 255),
                           randint(0, 255)))
        qp.drawEllipse(130, 400, 20 * size, 20 * size)
        qp.setBrush(QColor(randint(0, 255),
                           randint(0, 255),
                           randint(0, 255)))
        size = randint(1, 3)
        qp.drawEllipse(600, 200, 20 * size, 20 * size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
