from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from logics.Authentication import Authentication

class SignUpView(QWidget):
    def __init__(self, signUpCallBack):
        super().__init__()
        self.setWindowTitle("SignUp")
        self.auth = Authentication()
        self.signCallBack = signUpCallBack

        self.initUI()
    
    def initUI(self):
        layoutV = QVBoxLayout()

        title = QLabel("Sign Up")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        self.idInput = QLineEdit()
        self.idInput.setPlaceholderText("ID 입력")
        
        self.pwInput = QLineEdit()
        self.pwInput.setPlaceholderText("비밀번호 입력")
        self.pwInput.setEchoMode(QLineEdit.Password)

        self.confirmInput = QLineEdit()
        self.confirmInput.setPlaceholderText("비밀번호 확인")
        self.confirmInput.setEchoMode(QLineEdit.Password)

        signUpBtn = QPushButton("가입하기")
        signUpBtn.clicked.connect(self.handleSignup)

        backBtn = QPushButton("뒤로가기")
        backBtn.clicked.connect(self.signCallBack)

        layoutV.addWidget(title)
        layoutV.addWidget(self.idInput)
        layoutV.addWidget(self.pwInput)
        layoutV.addWidget(self.confirmInput)
        layoutV.addWidget(signUpBtn)
        layoutV.addWidget(backBtn)

        self.setLayout(layoutV)
        
    def handleSignup(self):
        user = self.idInput.text().strip()
        pw = self.pwInput.text().strip()
        confirm = self.confirmInput.text().strip()

        if not user or not pw or not confirm:
            QMessageBox.warning(self, "오류", "모든 필드를 입력해주세요.")
            return
        
        if pw != confirm:
            QMessageBox.warning(self, "오류", "비밀번호가 입력되지 않았습니다.")
            return

        if self.auth.register(user, pw):
            QMessageBox.information(self, "완료", "회원가입 성공, 로그인 해주세요.")
            self.signCallBack()
        else:
            QMessageBox.warning(self, "실패", "존재하는 ID입니다.")