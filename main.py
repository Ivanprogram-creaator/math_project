from PyQt5.QtWidgets import QApplication, QMainWindow
# from app.main_window import Window
from app.window import Ui_MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    Ui_MainWindow().setupUi(window)
    window.show()
    app.exec()