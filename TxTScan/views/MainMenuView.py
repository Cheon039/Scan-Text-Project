from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainMenuView(QWidget):
    def __init__(self, goInputText, goUpload, goResult, goSave, logout):
        super().__init__()
        self.goInputText = goInputText
        self.goUpload = goUpload
        self.goResult = goResult
        self.goSave = goSave
        self.logout = logout

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        tooBar = QHBoxLayout()
        tooBar.addStretch()
        logoutBtn = QPushButton("로그아웃")
        logoutBtn.clicked.connect(self.logout)
        tooBar.addWidget(logoutBtn)
        layout.addLayout(tooBar)

        title = QLabel("TXT Scan Main Menu")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        uploadBtn = QPushButton("문서 / 이미지 업로드")
        inputBtn = QPushButton("텍스트 직접 입력")
        resultBtn = QPushButton("최신 결과 보기")
        saveViewBtn = QPushButton("결과 저장 목록")

        uploadBtn.clicked.connect(self.goUpload)
        inputBtn.clicked.connect(self.goInputText)
        resultBtn.clicked.connect(lambda: self.goResult(None))
        saveViewBtn.clicked.connect(self.goSave)
        logoutBtn.clicked.connect(self.logout)

        layout.addWidget(title)
        layout.addWidget(uploadBtn)
        layout.addWidget(inputBtn)
        layout.addWidget(resultBtn)
        layout.addWidget(saveViewBtn)

        self.setLayout(layout)