from PySide6 import QtCore, QtWidgets, QtGui

def hanoi(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target, moves)
    moves.append(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source, moves)
    
class CenterDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        option.displayAlignment = QtCore.Qt.AlignCenter
        font = painter.font()
        font.setPointSize(36)
        painter.setFont(font)
        super().paint(painter, option, index)
        
class CustomValidator(QtGui.QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, input, pos):
        if input == "":
            return QtGui.QValidator.Intermediate, input, pos
        if input.isdigit():
            # Verifica che il numero sia maggiore di zero
            if int(input) > 0 and int(input) < 20:
                return QtGui.QValidator.Acceptable, input, pos
            else:
                return QtGui.QValidator.Invalid, input, pos
        return QtGui.QValidator.Invalid, input, pos