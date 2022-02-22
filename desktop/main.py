import sys
import pyqtgraph as pg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from GUI.GUI import Ui_MainWindow


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()

        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionNew.triggered.connect(self.new_instance)

    def new_instance(self) -> None:
        self.child_window = MainWindow()
        self.child_window.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
