import os
import sys

import requests
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

SCREEN_SIZE = [600, 450]

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.z = 10
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.lat = 37.530887
        self.lot = 55.703118
        self.spn = [0.01, 0.01]
        self.getImage()
        self.initUI()

    def getImage(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll\
={self.lat},{self.lot}&spn={self.spn[0]},{self.spn[1]}&l=map"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap(self.map_file)

        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == 16777238:
            self.spn[0] *= 2
            self.spn[1] *= 2
        elif event.key() == 16777239:
            self.spn[0] /= 2
            self.spn[1] /= 2
        elif event.key() == 16777235:
            self.lot += 2 * self.spn[0]
        # self.spn[0] *= 10
        elif event.key() == 16777234:
            self.lat -= 2.6 * self.spn[1]
        # self.spn[1] /= 10
        elif event.key() == 16777237:
            self.lot -= 2 * self.spn[0]
        # self.spn[0] /= 10
        elif event.key() == 16777236:
            self.lat += 2.6 * self.spn[1]
        # self.spn[1] *= 10
        self.getImage()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
