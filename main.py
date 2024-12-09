import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 400)
        self.pushButton = QPushButton('НАЖМИ', self)
        self.pushButton.move(150, 300)
        self.flag = False
        self.pushButton.clicked.connect(self.draw_flag)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            x = random.randint(1, 200)
            y = random.randint(1, 200)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x, x, y, y)
            qp.end()

    def draw_flag(self, qp):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())