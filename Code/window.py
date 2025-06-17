from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtCore import QTimer

from Code.functions import *


class Window(QWidget):
    def __init__(self, SCREEN_SIZE, color):
        super().__init__()
        self.X, self.Y = SCREEN_SIZE.width(), SCREEN_SIZE.height()
        self.dx, self.dy = gen_coords(), gen_coords()
        self.count = 0
        self.color = color

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.moves)

        self.initUI()
        self.timer.start(INTERVAL)

    def initUI(self):
        start_coords = get_start_coords(self.X, self.Y)
        self.setGeometry(*start_coords, SIZE, SIZE)
        self.setWindowTitle('Ключик')

        self.pixmap = QPixmap('data/default_key.png')
        self.pixmap.scaled(SIZE, SIZE)

        self.image = QLabel(self)
        self.image.setStyleSheet(f"background-color: {COLORS[self.color]};")
        self.image.move(0, 0)
        self.image.resize(SIZE, SIZE)
        self.image.setPixmap(self.pixmap)

    def moves(self):
        self.count += 1
        pos = self.pos()
        x, y = pos.x(), pos.y()
        self.move(x + self.dx, y + self.dy)

        if self.pos().x() <= 0 or (self.pos().x() + SIZE) >= self.X:
            self.dx *= -1
        if self.pos().y() <= 0 or (self.pos().y() + SIZE) >= self.Y:
            self.dy *= -1

        if self.count == STOP_NUM:
            self.timer.stop()