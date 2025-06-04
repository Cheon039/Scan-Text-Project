import sys
from PyQt5.QtWidgets import QApplication
from ui.LoginView import LoginView

if __name__ == "__main__":
    txtScan = QApplication(sys.argv)
    window = LoginView()
    window.show()
    sys.exit(txtScan.exec_())