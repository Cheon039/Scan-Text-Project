# LoginView

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFrame)
from PyQt5.QtGui import QFont, QCursor # 글꼴, 커서 모양
from PyQt5.QtCore import Qt # 정렬, 마우스, 키보드 등

class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TxT Scan Login")
        self.setFixedSize(350, 250)
        self.setupUI()

    def setupUI(self):
        title = QLabel("TXT Scan")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        idLabel = QLabel("ID")
        self.idInput = QLineEdit()

        pwLabel = QLabel("PW")
        self.pwInput = QLineEdit()
        self.pwInput.setEchoMode(QLineEdit.Password)

        self.errorLabel = QLabel("")
        
        self.errorLabel.setAlignment(Qt.AlignCenter)

        signupLabel = QLabel('<a href="#">Sign up</a>')
        signupLabel.setTextFormat(Qt.RichText)
        signupLabel.setTextInteractionFlags(Qt.TextBrowserInteraction)
        signupLabel.setOpenExternalLinks(False)
        signupLabel.setStyleSheet("color: purple;")
        signupLabel.setCursor(QCursor(Qt.PointingHandCursor))
        signupLabel.linkActivated.connect(self.handleSignup)

        loginButton = QPushButton("확인")
        loginButton.clicked.connect(self.handleLogin)

        loginBox = QFrame()
        loginLayout = QVBoxLayout()
        loginLayout.addWidget(idLabel)
        loginLayout.addWidget(self.idInput)
        loginLayout.addWidget(pwLabel)
        loginLayout.addWidget(self.pwInput)
        loginLayout.addWidget(self.errorLabel)

        btmLayout = QHBoxLayout()
        btmLayout.addWidget(signupLabel)
        btmLayout.addStretch()
        btmLayout.addWidget(loginButton)

        loginLayout.addLayout(btmLayout)
        loginBox.setLayout(loginLayout)
        loginBox.setStyleSheet("background-color: #ddd; padding: 3px;")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(title)
        mainLayout.addWidget(loginBox)

        self.setLayout(mainLayout)

    def handleLogin(self):
        user = self.idInput.text()
        pw = self.pwInput.text()

        if user == "user" and pw == "1234":
            self.errorLabel.setText("")
            self.errorLabel.setStyleSheet("color: blue;")
            self.errorLabel.setText("로그인 성공")
            # TODO: 메인 메뉴 이동
        else:
            self.errorLabel.setStyleSheet("color: red;")
            self.errorLabel.setText("아이디 또는 비밀번호가 잘못되었습니다.")

        print("로그인 시도:", self.idInput.text())

    def handleSignup(self):
        print("회원가입 링크 클릭")