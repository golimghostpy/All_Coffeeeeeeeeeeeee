import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.db")
        self.show_info()

    def show_info(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        self.show_coffee.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        else:
            self.show_coffee.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.show_coffee.setHorizontalHeaderLabels(['id', 'Название', 'Обжарка', 'Тип', 'Вкус', 'Цена', 'Объем'])
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.show_coffee.setItem(i, j, QTableWidgetItem(str(val)))
            self.modified = {}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())