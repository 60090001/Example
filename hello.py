import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from program3_1 import Ui_Form

def say_hello():
    print("Hello!")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    Form=QWidget()
    ui=Ui_Form()
    ui.setupUi(Form)
    ui.hello_button.clicked.connect(say_hello)
    Form.show()

    sys.exit(app.exec_())