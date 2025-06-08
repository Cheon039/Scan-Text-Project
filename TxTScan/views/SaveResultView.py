from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from logics.ResultManager import ResultManager
from PyQt5.QtWidgets import QMessageBox

class SaveResultView(QWidget):
    def __init__(self, user, goBack):
        super().__init__()
        self.user = user
        self.goBack = goBack
        self.manager = ResultManager(user)
        self.setWindowTitle("저장된 결과 목록")

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.listWidget = QListWidget()
        self.detailBox = QTextEdit()
        self.detailBox.setReadOnly(True)

        self.backBtn = QPushButton("돌아가기")
        self.backBtn.clicked.connect(self.goBack)

        self.deleteBtn = QPushButton("선택 삭제")  # ✅ 추가
        self.deleteBtn.clicked.connect(self.handleDelete)   

        layout.addWidget(QLabel("📄 저장된 결과 목록:"))
        layout.addWidget(self.listWidget)
        layout.addWidget(QLabel("📝 상세 내용:"))
        layout.addWidget(self.detailBox)
        layout.addWidget(self.deleteBtn)
        layout.addWidget(self.backBtn)

        self.setLayout(layout)
        self.loadResults()

        self.listWidget.currentRowChanged.connect(self.showDetail)

    def loadResults(self):
        self.results = self.manager.getResultList()
        self.listWidget.clear()
        for idx, item in enumerate(self.results):
            preview = item.strip().split("\n")[0][:30]
            self.listWidget.addItem(f"{idx+1}. {preview}...")

    def showDetail(self, index):
        if index >= 0:
            fullText = self.manager.getResult(index)  # ✅ 실제 전체 텍스트 로드
            self.detailBox.setText(fullText)
        else:
            self.detailBox.clear()

    def handleDelete(self):
        current = self.listWidget.currentRow()
        if current >= 0:
            confirm = QMessageBox.question(
                self, "삭제 확인", "선택한 결과를 삭제하시겠습니까?",
                QMessageBox.Yes | QMessageBox.No
            )
            if confirm == QMessageBox.Yes:
                success = self.manager.deleteResult(current)
                if success:
                    QMessageBox.information(self, "삭제 완료", "결과가 삭제되었습니다.")
                    self.loadResults()         # ✅ 목록 다시 로드
                    self.detailBox.clear()     # ✅ 상세 내용도 지움
                else:
                    QMessageBox.warning(self, "삭제 실패", "결과를 삭제하지 못했습니다.")
        else:
            QMessageBox.warning(self, "선택 없음", "삭제할 결과를 선택하세요.")