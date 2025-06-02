import sys
from PyQt5.QtWidgets import QApplication
from ui.LoginView import LoginView

if __name__ == "__main__":
    print(1 + 2)
    txtScan = QApplication(sys.argv)
    window = LoginView()
    window.show()
    sys.exit(txtScan.exec_())