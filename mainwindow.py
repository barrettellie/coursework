#create the main window

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class MainWindow(QMainWindow):
    """simple example using QtSql""" #doc string
    #constructor
    def __init__(self):
        #calls the super class constructor
        super().__init__()

        self.stackedLayout = QStackedLayout()
        self.create_initial_layout()
        self.stackedLayout.addWidget(self.initial_layout_widget)
        self.central_widget = QWidget()

        self.central_widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.central_widget)

        #connection to the database
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("coffee_shop.db")
        self.db.open()

        self.table_view = QTableView()

    def create_initial_layout(self):
        self.welcome_message = QLabel("Bed and Breakfast Payroll System")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.welcome_message)

        self.initial_layout_widget = QWidget()
        self.initial_layout_widget.setLayout(self.layout)

        
        
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
