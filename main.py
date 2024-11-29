import random
import sys

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.radius = 0
        self.button.clicked.connect(self.create_random_circle)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        if self.radius > 0:
            painter.drawEllipse((self.width() - 2 * self.radius) // 2,
                                (self.height() - 2 * self.radius) // 2,
                                2 * self.radius, 2 * self.radius)

    def create_random_circle(self):
        self.radius = random.randint(5, 100)
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
