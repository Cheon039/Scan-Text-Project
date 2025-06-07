from PyQt5.QtWidgets import (
    QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class InputTextView(QWidget):
    def __init__(self, dataController, goResult, goBack):
        super().__init__()
        self.dataController = dataController
        self.goResult = goResult
        self.goBack = goBack
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.textEdit = QTextEdit()
        self.textEdit.setPlaceholderText("요약/번역할 텍스트를 입력하세요.")
        layout.addWidget(self.textEdit)

        btnLayout = QHBoxLayout()
        startBtn = QPushButton("요약 / 번역 실행")
        clearBtn = QPushButton("초기화")
        cancelBtn = QPushButton("취소")
        btnLayout.addWidget(startBtn)
        btnLayout.addWidget(clearBtn)
        btnLayout.addWidget(cancelBtn)

        layout.addLayout(btnLayout)

        startBtn.clicked.connect(self.handleProcess)
        clearBtn.clicked.connect(self.textEdit.clear)
        cancelBtn.clicked.connect(self.goBack)

        self.setLayout(layout)

    def handleProcess(self):
        text = self.textEdit.toPlainText().strip()
        if not text:
            return  # 나중에 QMessageBox로 '텍스트 없음' 표시 가능

        result = self.dataController.process(text)
        self.goResult(result)