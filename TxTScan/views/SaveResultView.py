from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from logics.ResultManager import ResultManager
from PyQt5.QtWidgets import QMessageBox

class SaveResultView(QWidget):
    def __init__(self, user, goBack):
        super().__init__()
        self.user = user
        self.goBack = goBack
        self.resultManager = ResultManager(user)
        self.setWindowTitle("저장된 결과 목록")

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.list = QListWidget()
        self.detailBox = QTextEdit()
        self.detailBox.setReadOnly(True)

        self.backBtn = QPushButton("돌아가기")
        self.backBtn.clicked.connect(self.goBack)

        self.delBtn = QPushButton("선택 삭제") 
        self.delBtn.clicked.connect(self.handleDelete)   

        layout.addWidget(QLabel("저장된 결과 목록:"))
        layout.addWidget(self.list)
        layout.addWidget(QLabel("상세 내용:"))
        layout.addWidget(self.detailBox)
        layout.addWidget(self.delBtn)
        layout.addWidget(self.backBtn)

        self.setLayout(layout)
        self.loadResults()

        self.list.currentRowChanged.connect(self.showDetail)

    # 저장 결과 Load
    def loadResults(self):
        self.results = self.resultManager.getResultList()
        self.list.clear()
        for idx, item in enumerate(self.results):
            preview = item.strip().split("\n")[0][:30]
            self.list.addItem(f"{idx + 1}. {preview}...")

    # 상세 저장 내용 보기
    def showDetail(self, index):
        if index >= 0:
            fullText = self.resultManager.getResult(index)  # 전체 텍스트 로드
            self.detailBox.setText(fullText)
        else:
            self.detailBox.clear()

    # 결과 삭제 하기
    def handleDelete(self):
        current = self.list.currentRow()
        if current >= 0:
            confirm = QMessageBox.question(self, "삭제 확인", "선택한 결과를 삭제하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                success = self.resultManager.deleteResult(current)
                if success:
                    QMessageBox.information(self, "삭제 완료", "결과가 삭제되었습니다.")
                    self.loadResults()         # 목록 다시 로드
                    self.detailBox.clear()     # 상세 내용도 지움
                else:
                    QMessageBox.warning(self, "삭제 실패", "결과를 삭제하지 못했습니다.")
        else:
            QMessageBox.warning(self, "선택 없음", "삭제할 결과를 선택하세요.")