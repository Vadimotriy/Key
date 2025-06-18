from Code.constants import *
from Code.window import Window


class Manager():
    def __init__(self, screen_size):
        self.placed = 0
        self.windows = []
        for i in range(NUMBER):
            win = Window(screen_size, i)
            win.placed.connect(self.all_placed)
            win.show()
            self.windows.append(win)

    def start(self):
        for win in self.windows:
            win.timer.start(INTERVAL)

    def all_placed(self):
        self.placed += 1
        if self.placed == NUMBER:
            for win in self.windows:
                win.start_angel()