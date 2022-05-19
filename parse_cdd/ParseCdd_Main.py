
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from cdd import mainClass
from parsecdd import Ui_Mainform


class parsecddUi(QMainWindow,Ui_Mainform):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.openfile.clicked.connect(self.choose_file)
        self.filepath.textChanged[str].connect(self.onChanged)
        self.start.clicked.connect(self.create_sqc_crc)

    def onChanged(self, value):
        self.filepath.setText(value)

    def choose_file(self):
        retVal = QFileDialog.getOpenFileName(self, 'Open file',
                                                       "", '*.cdd')
        if retVal:
            self.fname = retVal[0]
            print(self.fname)
            if self.fname:
                self.filepath.setText(self.fname)


    def create_sqc_crc(self):
        c = mainClass()
        c.parseCdd(self.filepath.text())
        self.doors_text.setText(c.diagCan)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    demo=parsecddUi()
    demo.show()
    sys.exit(app.exec_())
