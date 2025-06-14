import os
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
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
        layoutV = QVBoxLayout()
        layoutH = QHBoxLayout()
        layoutH.addStretch()
        logoutBtn = QPushButton("로그아웃")
        logoutBtn.clicked.connect(self.logout)
        layoutH.addWidget(logoutBtn)
        layoutV.addLayout(layoutH)

        # 로고 삽입
        currentDir = os.path.dirname(os.path.abspath(__file__))
        logoPath = os.path.join(currentDir, "ScanLogo.png")

        logoLabel = QLabel()
        logoPixmap = QPixmap(logoPath)

        logoPixmap = logoPixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logoLabel.setPixmap(logoPixmap)

        logoLabel.setAlignment(Qt.AlignCenter)

        layoutV.addWidget(logoLabel)


        uploadBtn = QPushButton("문서 / 이미지 업로드")
        inputBtn = QPushButton("텍스트 직접 입력")
        resultBtn = QPushButton("최신 결과 보기")
        saveViewBtn = QPushButton("결과 저장 목록")

        uploadBtn.clicked.connect(self.goUpload)
        inputBtn.clicked.connect(self.goInputText)
        resultBtn.clicked.connect(lambda: self.goResult(None))
        saveViewBtn.clicked.connect(self.goSave)
        logoutBtn.clicked.connect(self.logout)

        layoutV.addWidget(uploadBtn)
        layoutV.addWidget(inputBtn)
        layoutV.addWidget(resultBtn)
        layoutV.addWidget(saveViewBtn)

        self.setLayout(layoutV)