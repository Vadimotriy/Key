from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import  QLabel, QWidget

from Code.constants import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, SIZE, SIZE)
        self.setWindowTitle('Ключик')

        self.pixmap = QPixmap('data/default_key.jpg')
        self.pixmap.scaled(SIZE, SIZE)

        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(SIZE, SIZE)
        self.image.setPixmap(self.pixmap)

    def moves(self):
        self.move(5, 5)