# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.LoginView import LoginView
from views.SignUpView import SignUpView
from views.MainMenuView import MainMenuView


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TXT Scan")
        self.setGeometry(100, 100, 800, 600)  # 초기 창 크기

        self.showLoginView()

    def showLoginView(self):
        loginView = LoginView(goSignup=self.showSignUpView, goMainMenu=self.showMainMenuView)
        self.setCentralWidget(loginView)

    def showSignUpView(self):
        signupView = SignUpView(signupCallBack=self.showLoginView)
        self.setCentralWidget(signupView)

    def showMainMenuView(self):
        menuView = MainMenuView(
            goInputText=self.showInputTextView,
            goUpload=self.showUploadView,
            goResult=self.showResultView,
            goSave=self.showSaveResultView,
            logout=self.showLoginView
        )
        self.setCentralWidget(menuView)

    def showInputTextView(self):
        print("InputTextView로 이동 (아직 구현 안됨)")

    def showUploadView(self):
        print("UploadView로 이동 (아직 구현 안됨)")

    def showResultView(self):
        print("ResultView로 이동 (아직 구현 안됨)")

    def showSaveResultView(self):
        print("SaveResultView로 이동 (아직 구현 안됨)")

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()