import sys
from PyQt6.QtWidgets import QApplication

from Code.windows.manager import Manager

if __name__ == '__main__':
    app = QApplication(sys.argv)
    SCREEN_SIZE = QApplication.primaryScreen().size()
    manager = Manager(SCREEN_SIZE)
    manager.start()
    app.exec()
