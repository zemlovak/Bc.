import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QGridLayout, QWidget
from PyQt5.QtCore import QSize

class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(300, 60))
        self.setWindowTitle("PyQt")
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        hello = QPushButton("Hello World!", self)
        hello.clicked.connect(self.hellofcn)
        close = QPushButton("Close", self)
        close.clicked.connect(self.close)
        label = QLabel("My first GUI")
        label.setIndent(100)

        gridLayout.addWidget(label, 0, 0)
        gridLayout.addWidget(hello, 1, 0)
        gridLayout.addWidget(close, 2, 0)

    def hellofcn(self):
        print("Hello world!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )