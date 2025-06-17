from PyQt6.QtWidgets import QApplication


SIZE = 200
MOVEMENT = 5
INTERVAL = 10
STOP_NUM = (1000 / INTERVAL) * 10
COLORS = [
    "#FF0000",  # Красный
    "#FFA500",  # Оранжевый
    "#FFFF00",  # Жёлтый
    "#00FF00",  # Зелёный
    "#00FFFF",  # Голубой
    "#0000FF",  # Синий
    "#8A2BE2"   # Фиолетовый
]


for screen in QApplication.screens():
    print(screen)