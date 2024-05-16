import sys
from PySide6 import QtCore, QtWidgets, QtGui
import utils
import resultWindow
from utils import CustomValidator, CenterDelegate
            
class mainWindow(QtWidgets.QWidget):
    #defining the interface
    def __init__(self):
        super().__init__()
        self.setStyleSheet("font: 18pt Roboto; background-color: #2B2B2B;")
        self.startButton = QtWidgets.QPushButton("Start")
        self.startButton.setStyleSheet("background-color: white; color:black;")
        self.startButton.setFixedSize(100,50)
        
        self.title = QtWidgets.QLabel("Welcome to Hanoi's Tower solver! \n\n Please tell me the number of disks you want and select the target")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        
        self.image = QtGui.QPixmap("images/Hanoi.png")
        self.imageLab = QtWidgets.QLabel()
        imageScaled = self.image.scaledToWidth(350)
        self.imageLab.setPixmap(imageScaled)
        
        self.input = QtWidgets.QLineEdit()
        validator = CustomValidator()
        self.input.setValidator(validator)
        self.input.setFixedSize(300,25)
        self.input.setPlaceholderText("Number of disks (1-19)")
        
        label = QtWidgets.QLabel("Target:")
        self.target = QtWidgets.QComboBox()
        self.target.addItem("B")
        self.target.addItem("C")
        self.target.setFixedWidth(75)
        
        self.subLayout = QtWidgets.QVBoxLayout()
        self.subLayout.addWidget(label)
        self.subLayout.addWidget(self.target)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.horLayout = QtWidgets.QHBoxLayout()
        self.horLayout.addWidget(self.input)
        self.horLayout.addLayout(self.subLayout)
        #self.horLayout.addWidget(self.target)
        self.layout.addWidget(self.imageLab,alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.title, alignment=QtCore.Qt.AlignTop)
        self.layout.addStretch()
        
        self.layout.addLayout(self.horLayout)
        #self.layout.addWidget(self.input, alignment=QtCore.Qt.AlignCenter)
        self.layout.addStretch()
        self.layout.addWidget(self.startButton, alignment=QtCore.Qt.AlignCenter)
        self.layout.addStretch()
        
        self.secondWindow = None 
        self.startButton.clicked.connect(self.start)
        
    def start(self):
        #Setting the game
        n = int(self.input.text())
        target = self.target.currentText()
        moves = []
        self.secondWindow = resultWindow.resultWindow(self )
        self.secondWindow.resize(1000, 800)
        self.secondWindow.show()
        self.close()
        
        if target == 'B':
            utils.hanoi(n, 'A', 'B', 'C', moves)
        else:
            utils.hanoi(n, 'A', 'C', 'B', moves)

        for i, move in enumerate(moves, 1):
            self.secondWindow.list.addItem(f"step {i}: {move}")
        
        delegate = CenterDelegate()
        self.secondWindow.list.setItemDelegate(delegate)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = mainWindow()
    widget.resize(1000, 800)
    widget.show()
    sys.exit(app.exec())