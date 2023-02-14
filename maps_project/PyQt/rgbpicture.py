import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton
from PyQt5 import uic
from PIL import Image

SCREEN_SIZE = [600, 420]


class Example(QMainWindow):
    pushButton: QPushButton
    pushButton_2: QPushButton
    pushButton_3: QPushButton
    pushButton_4: QPushButton
    pushButton_5: QPushButton
    pushButton_6: QPushButton
    label: QLabel

    def __init__(self):
        super().__init__()
        self.namefile = None
        self.initUI()

    def get_file(self):
        filepath, some = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
                                                     'Картинка (*.jpg);;Все файлы (*)')
        return filepath

    def get_red(self):
        im = Image.open(self.namefile)
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        im.save('tmp.jpg')
        self.pixmap = QPixmap('tmp.jpg')
        self.im = self.label
        self.im.setPixmap(self.pixmap)

    def get_green(self):
        im = Image.open(self.namefile)
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        im.save('tmp.jpg')
        self.pixmap = QPixmap('tmp.jpg')
        self.im = self.label
        self.im.setPixmap(self.pixmap)

    def get_blue(self):
        im = Image.open(self.namefile)
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b
        im.save('tmp.jpg')
        self.pixmap = QPixmap('tmp.jpg')
        self.im = self.label
        self.im.setPixmap(self.pixmap)

    def get_all(self):
        im = Image.open(self.namefile)
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, b
        im.save('tmp.jpg')
        self.pixmap = QPixmap('tmp.jpg')
        self.im = self.label
        self.im.setPixmap(self.pixmap)

    def rotate_left(self):
        im1 = Image.open(self.namefile)
        im1 = im1.rotate(90)
        im1.save(self.namefile)
        im = Image.open("tmp.jpg")
        im = im.rotate(90)
        im.save('tmp.jpg')
        self.pixmap = QPixmap('tmp.jpg')
        self.im = self.label
        self.im.setPixmap(self.pixmap)

    def rotate_right(self):
        im1 = Image.open(self.namefile)
        im1 = im1.rotate(270)
        im1.save(self.namefile)
        im = Image.open("tmp.jpg")
        im = im.rotate(270)
        im.save('tmp.jpg')
        self.pixmap = QPixmap('tmp.jpg')
        self.im = self.label
        self.im.setPixmap(self.pixmap)

    def initUI(self):
        uic.loadUi('rgbsquare.ui', self)
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')
        self.namefile = self.get_file()
        self.pixmap = QPixmap(self.namefile)
        self.pushButton.clicked.connect(self.get_red)
        self.pushButton_2.clicked.connect(self.get_green)
        self.pushButton_3.clicked.connect(self.get_blue)
        self.pushButton_4.clicked.connect(self.get_all)
        self.pushButton_5.clicked.connect(self.rotate_right)
        self.pushButton_6.clicked.connect(self.rotate_left)
        im = Image.open(self.namefile)
        im.save("tmp.jpg")


        self.im = self.label
        self.im.setPixmap(self.pixmap)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())