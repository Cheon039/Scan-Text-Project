from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QApplication, QDesktopWidget
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
from logics.Authentication import Authentication

class LoginView(QWidget):
    def __init__(self, goSignup, goMainMenu):
        super().__init__()
        self.goSign = goSignup
        self.goMainMenu = goMainMenu
        self.auth = Authentication()
        self.setWindowTitle("TxT Scan Login")

        # 화면 해상도에 따른 크기 설정
        screen = QApplication.primaryScreen()
        screenSize = screen.size()
        width = int(screenSize.width() * 0.4)
        height = int(screenSize.height() * 0.4)
        self.resize(width, height)
        
        self.setupUI()

    def setupUI(self):
        title = QLabel("TxT Scan")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        idLabel = QLabel("ID")
        self.idInput = QLineEdit()

        pwLabel = QLabel("PW")
        self.pwInput = QLineEdit()
        self.pwInput.setEchoMode(QLineEdit.Password)

        self.errorLabel = QLabel("")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        signUpLabel = QLabel('<a href="#">Sign up</a>')
        signUpLabel.setTextFormat(Qt.RichText)
        signUpLabel.setTextInteractionFlags(Qt.TextBrowserInteraction)
        signUpLabel.setOpenExternalLinks(False)
        signUpLabel.setStyleSheet("color: purple;")
        signUpLabel.setCursor(QCursor(Qt.PointingHandCursor))
        signUpLabel.linkActivated.connect(self.handleSignup)

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
        btmLayout.addWidget(signUpLabel)
        btmLayout.addStretch()
        btmLayout.addWidget(loginButton)

        loginLayout.addLayout(btmLayout)
        loginBox.setLayout(loginLayout)
        loginBox.setStyleSheet("background-color: #ddd; padding: 1px;")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(title)
        mainLayout.addWidget(loginBox)
        self.setLayout(mainLayout)

    def handleLogin(self):
        user = self.idInput.text().strip()
        pw = self.pwInput.text().strip()

        if self.auth.verify(user, pw):  # 로그인 성공 조건
            self.errorLabel.setStyleSheet("color: blue;")
            self.errorLabel.setText("로그인 성공")
            self.goMainMenu()  # 메인메뉴로 이동
        else:
            self.errorLabel.setStyleSheet("color: red;")
            self.errorLabel.setText("아이디 또는 비밀번호가 잘못되었습니다.")

    def handleSignup(self):
        self.goSign()