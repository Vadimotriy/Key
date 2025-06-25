ACTIVATED = False

SIZE = 200
MOVEMENT = 5
INTERVAL = 10
STOP_NUM = (1000 / INTERVAL) * 1
NUMBER = 9

COLORS = [
    "#FF0000",  # Красный
    "#00FF00",  # Ярко-зелёный
    "#0000FF",  # Синий
    "#FFFF00",  # Жёлтый
    "#00FFFF",  # Голубой
    "#FFA500",  # Оранжевый
    "#8A2BE2",  # Фиолетовый (синеватый)
    "#FF69B4",  # Розовый
    "#ADFF2F",  # Зелёный с желтым оттенком
]
ANGLES = [360 / NUMBER * i for i in range(NUMBER)]

RADIUS = 3  # чем меньше тем больше радиус
STEP_ANGLE = 1  # чем больше тем быстрее крутится
