from pygame import mixer
from time import sleep

from Code.constants import *
from Code.windows.window import Window
from Code.windows.image import ImageWindow


class Sound():
    def __init__(self):
        mixer.init()
        self.sounds()

    def sounds(self):
        self.sound = mixer.Sound('data/sound.mp3')


class Manager():
    def __init__(self, screen_size):
        self.placed = 0
        self.windows = []
        self.sound = Sound()
        for i in range(NUMBER):
            win = Window(screen_size, i, self.sound)
            win.placed.connect(self.all_placed)
            win.joked.connect(self.close)
            win.show()
            self.windows.append(win)
        self.width, self.height = screen_size.width, screen_size.height

    def start(self):
        for win in self.windows:
            win.timer.start(INTERVAL)

    def all_placed(self):
        self.placed += 1
        if self.placed == NUMBER:
            for win in self.windows:
                win.start_angel()

    def close(self):
        for win in self.windows:
            if win.state:
                num = win.color
            win.close()

        exec(f'self.joke{num}()')

    def joke0(self):  # Звук на максимум
        for i in range(5):
            self.sound.sound.play()
        sleep(3)

    def joke2(self):  # Экран смерти
        new_window = ImageWindow('bluewindow', self.width(), self.height())
        new_window.show()
        self.windows.append(new_window)
