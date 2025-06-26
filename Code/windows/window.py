from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtCore import QTimer, pyqtSignal, Qt

from Code.functions import *
from Code.jokes import *


class Window(QWidget):
    placed = pyqtSignal()
    joked = pyqtSignal()

    def __init__(self, SCREEN_SIZE, color, sound):
        super().__init__()
        self.X, self.Y = SCREEN_SIZE.width(), SCREEN_SIZE.height()
        self.dx, self.dy = gen_coords(), gen_coords()
        self.sound = sound
        self.count = 0
        self.color = color
        self.angle = ANGLES[self.color]
        self.coords = calculate_coords(self.angle, self.X, self.Y)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.moves)

        self.initUI()

    def initUI(self):
        start_coords = get_start_coords(self.X, self.Y)
        self.setFixedSize(SIZE, SIZE)
        self.move(*start_coords)
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
            self.count = 0
            self.timer.stop()
            self.timer.disconnect()
            self.timer.timeout.connect(self.get_to_pos)
            self.timer.start(INTERVAL)

    def get_to_pos(self):
        pos = self.pos()
        x, y = move_x_y(pos.x(), pos.y(), self.coords)
        self.move(x, y)

        if x == self.coords[0] and y == self.coords[1]:
            self.timer.stop()
            self.placed.emit()

    def start_angel(self):
        self.timer.disconnect()
        self.timer.timeout.connect(self.angles)
        self.timer.start(INTERVAL)

    def angles(self):
        self.count += 1
        self.move(*calculate_coords(self.angle, self.X, self.Y))
        self.angle += STEP_ANGLE

        if self.count == STOP_NUM:
            self.timer.stop()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton or event.button() == Qt.MouseButton.RightButton:
            if not check():
                activated()
                self.joked.emit()

                exec(f'joke{self.color + 1}(self.X, self.Y, self.sound)')
