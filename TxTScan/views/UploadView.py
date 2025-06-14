from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QFileDialog, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt
import os
import fitz

class UploadView(QWidget):
    def __init__(self, dataController, goResult, goBack):
        super().__init__()
        self.dataController = dataController
        self.goResult = goResult
        self.goBack = goBack
        self.setWindowTitle("문서 / 이미지 업로드")
        self.initUI()

    def initUI(self):
        layoutV = QVBoxLayout()

        self.infoLabel = QLabel("문서 또는 이미지 파일을 업로드하세요.")
        self.resultBox = QTextEdit()
        self.resultBox.setReadOnly(True)

        btnLayout = QHBoxLayout()
        uploadBtn = QPushButton("파일 선택")
        processBtn = QPushButton("요약 / 번역")
        backBtn = QPushButton("돌아가기")

        uploadBtn.clicked.connect(self.handleUpload)
        processBtn.clicked.connect(self.handleProcess)
        backBtn.clicked.connect(self.goBack)

        btnLayout.addWidget(uploadBtn)
        btnLayout.addWidget(processBtn)
        btnLayout.addWidget(backBtn)

        layoutV.addWidget(self.infoLabel)
        layoutV.addWidget(self.resultBox)
        layoutV.addLayout(btnLayout)
        self.setLayout(layoutV)

        self.filePath = None

    # 파일 선택 버튼 클릭 시, 파일 선택창
    def handleUpload(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "파일 선택", "", "문서 및 이미지 (*.txt *.pdf *.jpg *.png *.jpeg);;모든 파일 (*)")
        if filePath:
            self.filePath = filePath
            self.infoLabel.setText(f"선택된 파일: {os.path.basename(filePath)}")
        else:
            self.infoLabel.setText("파일이 선택되지 않았습니다.")

    # PDF 파일의 텍스트 추출을 위한 함수
    def extractPDFText(self, filepath):
        doc = fitz.open(filepath)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    # 요약/번역 버튼 클릭 시 처리
    def handleProcess(self):
        if not self.filePath:
            QMessageBox.warning(self, "경고", "파일을 먼저 선택하세요.")
            return

        ext = os.path.splitext(self.filePath)[-1].lower()

        # 확장자에 따른 분기
        if ext in [".jpg", ".jpeg", ".png"]:
            extract = self.dataController.processOCR(self.filePath) # 이미지 OCR (OCR 미완성)
        elif ext == ".txt":
            with open(self.filePath, "r", encoding="utf-8") as f:
                extract = f.read()
        elif ext == ".pdf":
            extract = self.extractPDFText(self.filePath)
        else:
            QMessageBox.warning(self, "지원 안 됨", "현재는 txt, pdf, 이미지 파일만 지원합니다.")
            return

        if not extract.strip():
            QMessageBox.warning(self, "오류", "텍스트를 추출할 수 없습니다.")
            return

        result = self.dataController.process(extract)
        self.resultBox.setText(result)
        self.goResult(result)