import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


app = QApplication([])
gui = QWidget()
label = QLabel()
main_layout = QVBoxLayout()

gui.setWindowTitle("Party")
gui.setGeometry(50,50,500,300)

main_layout.addWidget(label)
gui.setLayout(main_layout)

label.setAlignment(Qt.AlignCenter) 

movie = QMovie("partyparrot.gif")

label.setMovie(movie)
movie.start() 

def foo(*args):
    print(args)

# movie.resized.connect(foo)

gui.show()
sys.exit(app.exec_()) 