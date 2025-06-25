from Code.constants import *
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


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
    pass


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
