# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from views.LoginView import LoginView
from views.SignUpView import SignUpView
from views.MainMenuView import MainMenuView
from views.InputTextView import InputTextView
from views.ResultView import ResultView
from logics.DataController import DataController
from views.SaveResultView import SaveResultView
from views.UploadView import UploadView

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TXT Scan")
        self.resize(800, 600)
        self.center()
        self.currentUser = None
        self.dataController = None
        self.lastResult = None
        self.showLoginView()

    def showLoginView(self):
        loginView = LoginView(goSignup=self.showSignUpView, goMainMenu=self.showMainMenuView)
        self.setCentralWidget(loginView)

    def showSignUpView(self):
        signupView = SignUpView(signupCallBack=self.showLoginView)
        self.setCentralWidget(signupView)

    def showMainMenuView(self):

        if  not self.dataController:
            self.currentUser = "user"
            self.dataController = DataController(self.currentUser)

        menuView = MainMenuView(
            goInputText=self.showInputTextView,
            goUpload=self.showUploadView,
            goResult=self.showResultView,
            goSave=self.showSaveResultView,
            logout=self.showLoginView
        )
        self.setCentralWidget(menuView)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showInputTextView(self):
        inputView = InputTextView(
        dataController=self.dataController,       # 핵심 처리 객체
        goResult=self.showResultView,             # 처리 후 결과 화면으로
        goBack=self.showMainMenuView              # '취소' 시 메인메뉴로 복귀
        )
        self.setCentralWidget(inputView)

    def showUploadView(self):
        print("UploadView로 이동 (아직 구현 안됨)")

    def showResultView(self, result=None):
        if result is not None and isinstance(result, str):
            self.lastResult = result  # ✅ 새로 들어온 결과 저장
        elif self.lastResult is None:
            print("[INFO] 표시할 결과가 없습니다.")
            self.lastResult = "[결과가 없습니다.]"

        resultView = ResultView(self.lastResult, goBack=self.showMainMenuView, dataController=self.dataController)
        self.setCentralWidget(resultView)

    def showSaveResultView(self):
        view = SaveResultView(self.currentUser, goBack=self.showMainMenuView)
        self.setCentralWidget(view)

    def showUploadView(self):
        uploadView = UploadView(
            dataController=self.dataController,
            goResult=self.showResultView,
            goBack=self.showMainMenuView
        )
        self.setCentralWidget(uploadView)

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()