import sys

from PyQt6.QtWidgets import QApplication
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

from Code.constants import *
from Code.windows.image import ImageWindow

def joke1(width, height, mixer):  # Звук на максимум
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(0.1, None)

    for i in range(5):
        mixer.sound.play()


def joke2(width, height, mixer):  # Звук на максимум
    pass


def joke3(width, height, mixer):  # Звук на максимум
    app = QApplication(sys.argv)
    new_window = ImageWindow('bluewindow', width, height)
    new_window.show()
    app.exec()


def joke4(width, height, mixer):  # Звук на максимум
    pass


def joke5(width, height, mixer):  # Звук на максимум
    pass


def joke6(width, height, mixer):  # Звук на максимум
    pass


def joke7(width, height, mixer):  # Звук на максимум
    pass


def joke8(width, height, mixer):  # Звук на максимум
    pass


def joke9(width, height, mixer):  # Звук на максимум
    pass
