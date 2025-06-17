import sys
from PyQt6.QtWidgets import QApplication

from Code.window import Window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    SCREEN_SIZE = QApplication.primaryScreen().size()
    print(SCREEN_SIZE)
    for i in range(7):
        exec(f'win{i} = Window(SCREEN_SIZE, {i})')
        exec(f'win{i}.show()')
    sys.exit(app.exec())