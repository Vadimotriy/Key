import sys
from PyQt6.QtWidgets import QApplication

from Code.window import Example


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    ex.moves()
    sys.exit(app.exec())