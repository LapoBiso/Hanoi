from PySide6 import QtCore, QtWidgets, QtGui

        
class resultWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setStyleSheet("font: 18pt Roboto; background-color: #2B2B2B;")
        self.endButton = QtWidgets.QPushButton("Home")
        self.endButton.setFixedSize(100,50)
        
        self.image = QtGui.QPixmap("images/Hanoi.png")
        self.imageLab = QtWidgets.QLabel()
        imageScaled = self.image.scaledToWidth(350)
        self.imageLab.setPixmap(imageScaled)
        
        self.title = QtWidgets.QLabel(f"Here it is the steps to solve the game with {parent.input.text()} disks")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        
        self.list = QtWidgets.QListWidget(self)
        self.list.setStyleSheet("font: 20pt Roboto; background-color: black;")
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.imageLab, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.title, alignment=QtCore.Qt.AlignTop)
        self.list.setSpacing(4)
        self.layout.addSpacing(20)
        self.layout.addWidget(self.list)
        self.layout.addWidget(self.endButton, alignment=QtCore.Qt.AlignCenter)
        self.endButton.clicked.connect(self.end)
        
    def end(self):
            self.close()
            if self.parent:
                self.parent.show()