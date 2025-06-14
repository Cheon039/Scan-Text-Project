from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication

class ResultView(QWidget):
    def __init__(self, resultText, originalText=None, goBack=None, dataController=None):
        super().__init__()
        self.goBack = goBack
        self.dataController = dataController  # ✅ 추가
        self.setWindowTitle("최근 결과 보기")
        self.initUI(resultText, originalText)

    def initUI(self, resultText, originalText):
        layout = QVBoxLayout()

        if originalText:
            originalBox = QTextEdit()
            originalBox.setReadOnly(True)
            originalBox.setPlainText(originalText)
            originalBox.setPlaceholderText("입력한 원문")
            layout.addWidget(originalBox)

        self.resultBox = QTextEdit()
        self.resultBox.setReadOnly(True)
        self.resultBox.setPlainText(resultText)
        self.resultBox.setPlaceholderText("요약/번역 결과")
        layout.addWidget(self.resultBox)

        btnLayout = QHBoxLayout()
        copyBtn = QPushButton("복사")
        saveBtn = QPushButton("저장")
        backBtn = QPushButton("돌아가기")

        btnLayout.addWidget(copyBtn)
        btnLayout.addWidget(saveBtn)
        btnLayout.addWidget(backBtn)

        layout.addLayout(btnLayout)

        copyBtn.clicked.connect(self.copyResult)
        saveBtn.clicked.connect(self.handleSave)
        backBtn.clicked.connect(self.handleBack)
        self.setLayout(layout)

    # 복사 버튼 클릭 시
    def copyResult(self):
        clipboard = self.resultBox.clipboard() if hasattr(self.resultBox, 'clipboard') else QApplication.clipboard()
        clipboard.setText(self.resultBox.toPlainText())
        QMessageBox.information(self, "복사 완료", "복사되었습니다.")

    # 뒤로가기 버튼 클릭 시 
    def handleBack(self):
        if self.goBack:
            self.goBack()

    # 저장 버튼 클릭 시
    def handleSave(self):
        text = self.resultBox.toPlainText().strip()
        if text:
            if self.dataController:
                self.dataController.saveResult(text)
                QMessageBox.information(self, "저장 완료", "결과가 저장되었습니다.")