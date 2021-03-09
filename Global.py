from PyQt5.QtGui import QFont

class Settings():
    def __init__(self):
        self.defaultFont = QFont("Microsoft YaHei", 9)
        self.defaultDanmuFont = QFont("Microsoft YaHei", 16)
        self.defaultPopupFont = QFont('Microsoft YaHei', 15, QFont.Bold)

settings = Settings()
