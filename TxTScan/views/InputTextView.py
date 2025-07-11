from PyQt5.QtWidgets import (
    QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
)

class InputTextView(QWidget):
    def __init__(self, dataController, goResult, goBack):
        super().__init__()
        self.dataController = dataController
        self.goResult = goResult
        self.goBack = goBack
        self.initUI()

    def initUI(self):
        layoutV = QVBoxLayout()

        self.textEdit = QTextEdit()
        self.textEdit.setPlaceholderText("요약/번역할 텍스트를 입력하세요.")
        layoutV.addWidget(self.textEdit)

        btnLayout = QHBoxLayout()
        startBtn = QPushButton("요약 / 번역 실행")
        clearBtn = QPushButton("초기화")
        cancelBtn = QPushButton("취소")
        btnLayout.addWidget(startBtn)
        btnLayout.addWidget(clearBtn)
        btnLayout.addWidget(cancelBtn)

        layoutV.addLayout(btnLayout)

        startBtn.clicked.connect(self.handleProcess)
        clearBtn.clicked.connect(self.textEdit.clear)
        cancelBtn.clicked.connect(self.goBack)

        self.setLayout(layoutV)

    # 요약/번역 버튼 클릭 시
    def handleProcess(self):
        text = self.textEdit.toPlainText().strip() # 입력한 텍스트 읽기
        if not text:
            return  # 텍스트 없을 경우 return

        result = self.dataController.process(text) # 요약/번역 실행
        self.goResult(result) 