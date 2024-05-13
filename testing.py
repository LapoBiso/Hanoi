import unittest
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from interface import mainWindow
from PySide6.QtTest import QTest

class TestMyWidget(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QtWidgets.QApplication(sys.argv)
        
    def setUp(self):
        self.widget = mainWindow()
        self.widget.resize(1000, 800)  # Set the initial size
        self.widget.show()  # Ensure the widget is shown
        
    def test_mainWidgets(self):
        #testing widgets in mainWindow
        self.assertIsNotNone(self.widget)
        self.assertIsNotNone(self.widget.startButton)
        self.assertIsNotNone(self.widget.input)
        self.assertIsNotNone(self.widget.target)
        self.assertIsNotNone(self.widget.title)
    
    def test_startclick(self):
        #testing startButton function in mainWindow
        self.widget.input.setText("4")
        self.assertIsNone(self.widget.secondWindow)
        QTest.mouseClick(self.widget.startButton, QtCore.Qt.LeftButton)
        #secondWindow and list widget created
        self.assertIsNotNone(self.widget.secondWindow)
        self.assertIsNotNone(self.widget.secondWindow.list)
    
    def test_solver(self):
        #testing operation of Hanoi solver; 2^n - 1 steps
        self.widget.input.setText("3")
        QTest.mouseClick(self.widget.startButton, QtCore.Qt.LeftButton)
        self.assertEqual(self.widget.secondWindow.list.count(),7)
        
    def test_dimension(self):
        self.assertEqual(self.widget.width(), 1000)
        self.assertEqual(self.widget.height(), 800)
    
    def test_resultWidgets(self):
        #testing existence widgets defined in resultWindow
        self.widget.input.setText("5")
        QTest.mouseClick(self.widget.startButton, QtCore.Qt.LeftButton)
        self.assertIsNotNone(self.widget.secondWindow.endButton)
        self.assertIsNotNone(self.widget.secondWindow.imageLab)
        self.assertEqual(self.widget.secondWindow.parent,self.widget)
        self.assertIsNotNone(self.widget.secondWindow.title)
    
    def test_endclick(self): 
        #testing endButton function in resultWindow
        self.widget.input.setText("6")
        QTest.mouseClick(self.widget.startButton, QtCore.Qt.LeftButton)
        #mainWindow closed after startButton clicked
        self.assertFalse(self.widget.isVisible()) 
        QTest.mouseClick(self.widget.secondWindow.endButton, QtCore.Qt.LeftButton)
        #mainWindow open and resultWindow closed after endButton clicked
        self.assertFalse(self.widget.secondWindow.isVisible())
        self.assertTrue(self.widget.isVisible())
        
if __name__ == '__main__':
    unittest.main()