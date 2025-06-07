from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QClipboard

class ResultView(QWidget):
    def __init__(self, resultText):
        super().__init__()
        self.setWindowTitle("결과 보기")
        self.initUI(resultText)

    def initUI(self, resultText):
        layout = QVBoxLayout()

        self.resultBox = QTextEdit()
        self.resultBox.setReadOnly(True)
        self.resultBox.setPlainText(resultText)
        layout.addWidget(self.resultBox)

        btnLayout = QHBoxLayout()
        copyBtn = QPushButton("복사")
        clearBtn = QPushButton("초기화")
        btnLayout.addWidget(copyBtn)
        btnLayout.addWidget(clearBtn)

        layout.addLayout(btnLayout)

        copyBtn.clicked.connect(self.copyResult)
        clearBtn.clicked.connect(self.clearResult)

        self.setLayout(layout)

    def copyResult(self):
        clipboard = self.resultBox.clipboard() if hasattr(self.resultBox, 'clipboard') else QApplication.clipboard()
        clipboard.setText(self.resultBox.toPlainText())
        QMessageBox.information(self, "복사 완료", "결과가 클립보드에 복사되었습니다.")

    def clearResult(self):
        self.resultBox.clear()