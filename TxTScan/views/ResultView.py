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
            origBox = QTextEdit()
            origBox.setReadOnly(True)
            origBox.setPlainText(originalText)
            origBox.setPlaceholderText("입력한 원문")
            layout.addWidget(origBox)

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

    def copyResult(self):
        clipboard = self.resultBox.clipboard() if hasattr(self.resultBox, 'clipboard') else QApplication.clipboard()
        clipboard.setText(self.resultBox.toPlainText())
        QMessageBox.information(self, "복사 완료", "결과가 클립보드에 복사되었습니다.")

    def handleBack(self):
        if self.goBack:
            self.goBack()

    def handleSave(self):
        text = self.resultBox.toPlainText().strip()
        if text:
            if self.dataController:
                self.dataController.saveResult(text)
                QMessageBox.information(self, "저장 완료", "결과가 저장되었습니다.")
            else:
                QMessageBox.warning(self, "저장 실패", "데이터 컨트롤러가 없습니다.")
        else:
            QMessageBox.warning(self, "저장 실패", "저장할 결과가 없습니다.")