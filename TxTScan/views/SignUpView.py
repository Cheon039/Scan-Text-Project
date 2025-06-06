from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from logics.Authentication import Authentication

class SignUpView(QWidget):
    def __init__(self, signupCallBack):
        super().__init__()
        self.setWindowTitle("SignUp")
        self.auth = Authentication()
        self.signCallBack = signupCallBack

        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()

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

        signupButton = QPushButton("가입하기")
        signupButton.clicked.connect(self.handleSignup)

        backButton = QPushButton("뒤로가기")
        backButton.clicked.connect(self.signCallBack)

        layout.addWidget(title)
        layout.addWidget(self.idInput)
        layout.addWidget(self.pwInput)
        layout.addWidget(self.confirmInput)
        layout.addWidget(signupButton)
        layout.addWidget(backButton)

        self.setLayout(layout)
        
    def handleSignup(self):
        user = self.idInput.text().strip()
        pw = self.pwInput.text().strip()
        confirm = self.confirmInput.text().strip()

        if not user or not pw or not confirm:
            QMessageBox.warning(self, "오류", "모든 필드를 입력하세요.")
            return
        
        if pw != confirm:
            QMessageBox.warning(self, "오류", "비밀번호가 입력되지 않았습니다.")
            return

        if self.auth.register(user, pw):
            QMessageBox.information(self, "완료", "회원가입 성공! 로그인 해주세요.")
            self.signCallBack()
        else:
            QMessageBox.warning(self, "실패", "이미 존재하는 ID입니다.")