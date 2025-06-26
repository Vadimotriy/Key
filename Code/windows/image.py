from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtCore import QTimer, pyqtSignal, Qt

from Code.constants import *


class ImageWindow(QWidget):
    def __init__(self, image_name, width, height):
        self.image_name = image_name
        self.width, self.height = width, height
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle('Бу!')

        self.pixmap = QPixmap(f'data/{self.image_name}.png')
        self.pixmap = self.pixmap.scaled(
            self.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation
        )

        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(self.size())
        self.image.setPixmap(self.pixmap)

        self.showFullScreen()
