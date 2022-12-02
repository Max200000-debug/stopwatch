import threading 
import time 
import select
import sys
import socket
from PyQt5.QtWidgets import QLabel, QGridLayout, QComboBox, QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget, QMainWindow, QAction, qApp, QTextEdit
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.stop = False
    
        self.Compteur = QLabel('0', self)
        self.Compteur.setText('Compteur:')
        
        text = QTextEdit('0', self)
        text.setText('0')
        
        lab = QLabel('0', self)
        
        start = QPushButton('start', self)
        stop = QPushButton('Stop', self)
        connect = QPushButton('Connect', self)
        quit = QPushButton('Quit', self)
        reset = QPushButton('Reset', self)
        start.clicked.connect(self.start_thread)
        stop.clicked.connect(self.stop_thread)

        grid.addWidget(lab, 0, 1, 1, 1)
        grid.addWidget(self.Compteur, 0, 0, 1, 1)
        grid.addWidget(text, 1, 0, 1, 2)
        grid.addWidget(start, 2, 0, 1, 2)
        grid.addWidget(reset, 3, 1, 1, 1)
        grid.addWidget(stop, 3, 0, 1, 1)
        grid.addWidget(connect, 4, 0, 1, 1)
        grid.addWidget(quit, 4, 1, 1, 1)

        quit.clicked.connect(self.quit)
        reset.clicked.connect(self.reset)
        connect.clicked.connect(self.connect)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Compteur')

        self.show()

    def start_thread(self):
        self.stop = False
        self.thread = threading.Thread(target=self.counting_thread)
        self.thread.start()

    def counting_thread(self):
        while not self.stop:
            time.sleep(1)
            self.text.setText(str(int(self.text.toPlainText()) + 1))


    def stop_thread(self):
        self.stop = True


    def reset(self):
        self.text.setText('0')

    def quit(self):
        self.close()

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((''))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())