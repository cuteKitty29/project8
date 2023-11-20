import sys
import random
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_Elipse(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_Elipse(self, qp):
        qp.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        l = random.randrange(0, 212)
        qp.drawEllipse(random.randrange(0, 350), random.randrange(0, 240), l, l)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
