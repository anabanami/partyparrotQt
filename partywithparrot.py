import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

def home(GUI):

    label = QLabel()
    main_layout = QVBoxLayout()
    movie = QMovie("partyparrot.gif")
    btn_start = QPushButton("start")
    btn_stop = QPushButton("stop")

    GUI.setWindowTitle("Party")
    GUI.setGeometry(50,50,500,300)
    GUI.setLayout(main_layout)

    main_layout.addWidget(label)
    main_layout.addWidget(btn_start)
    main_layout.addWidget(btn_stop)

    label.setMovie(movie)
    label.setAlignment(Qt.AlignCenter)

    def foo():
        print("resizing..")

    def stop_click(checked):
        movie.setPaused(True)
        print("had enough?")

    def start_click(checked):
        movie.start()
        print("party time")

    movie.resized.connect(foo)    

    btn_stop.clicked.connect(stop_click)
    btn_start.clicked.connect(start_click)


def main():
    app = QApplication([])
    program = QWidget()
    
    home(program)

    program.show()
    app.exec_()


if __name__ =="__main__":
    main()