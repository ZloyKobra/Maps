import os
import sys

import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QRadioButton

SCREEN_SIZE = [600, 450]


class Example(QMainWindow, QApplication):
    pushButton: QPushButton
    lang: QLineEdit
    lat: QLineEdit
    image: QLabel
    map: QRadioButton
    satellite: QRadioButton
    gybrid: QRadioButton


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('ui.ui', self)
        self.setWindowTitle('Отображение карты')
        self.pushButton.clicked.connect(self.getImage)

    def getImage(self):
        api_server = "http://static-maps.yandex.ru/1.x/"

        lon = self.lang.text()
        lat = self.lat.text()
        delta = "0.002"

        params = {
            "ll": ",".join([lon, lat]),
            "spn": ",".join([delta, delta]),
            "l": self.get_map_view()
        }
        response = requests.get(api_server, params=params)

        if not response:
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.showMap()

    def showMap(self):
        self.pixmap = QPixmap(self.map_file)
        self.image.setPixmap(self.pixmap)

    def get_map_view(self):
        if self.map.isChecked():
            return "map"
        elif self.satellite.isChecked():
            return "sat"
        return "sat,skl"


    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())