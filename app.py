import requests, random, sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QVBoxLayout
from PyQt6.QtGui import QPixmap, QColor, QPalette
import pokebase as pb
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)


class Background(QLabel):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('blue'))
        self.setPalette(palette)
            

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Pocket Monsters")
        self.setFixedSize(200, 200)
        self.filename = ''
        self.pokemon = QLabel(self)
        self.get_new_pokemon()
        pixmap = QPixmap(self.filename)
        self.pokemon.setPixmap(pixmap)
        button = QPushButton(text="Reroll Pokemon", parent=self)
        layout = QVBoxLayout()
        layout.addWidget(self.pokemon)
        layout.addWidget(button)
        button.setFixedHeight(60)
        self.pokemon.setAlignment(Qt.AlignmentFlag.AlignHCenter)        
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)                
        button.pressed.connect(self.get_new_pokemon)                

    def get_new_pokemon(self):
        poke_id = random.randint(1,134)
        sprite = pb.SpriteResource('pokemon', poke_id, front_default = True)
        self.filename = '/images/%d.png' % poke_id
        with open(self.filename, 'wb') as f:
            f.write(requests.get(sprite.url).content)
        
        pixmap = QPixmap(self.filename)
        self.pokemon.setPixmap(pixmap)
        self.setWindowIcon = self.pokemon

        
window = MainWindow()
window.show()
app.exec()