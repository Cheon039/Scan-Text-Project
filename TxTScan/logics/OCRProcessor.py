# logics/OCRProcessor.py

import pytesseract
import shutil
import json
import os

class OCRProcessor:
    def __init__(self):
        self.imagePath = None
        self.resultText = ""
        self.language = "kor"

        # tesseract 경로 탐색
        tesseractCmd = shutil.which("tesseract")

        # 기본 경로
        if not tesseractCmd:
            defaultPath = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
            if os.path.exists(defaultPath):
                tesseractCmd = defaultPath

        # config에 경로 기록하기
        configPath = "config.json"
        if tesseractCmd:
            try:
                with open(configPath, "w") as f:
                    json.dump({"tesseract_path": tesseractCmd}, f, indent=2)
            except Exception as e:
                print(f"[OCRProcessor] config 생성 실패: {e}")

        # Tesseract 실행 경로 검증
        if not tesseractCmd or not os.path.exists(tesseractCmd):
            raise FileNotFoundError("Tesseract 실행 파일을 찾을 수 없습니다. 시스템 PATH 또는 config.json을 확인하세요.")

        pytesseract.pytesseract.tesseract_cmd = tesseractCmd # pytesseract에 경로 연결

    # 이미지 경로 설정
    def setImagePath(self, path):
        self.imagePath = path

    # 언어 설정
    def setLanguage(self, lang):
        self.language = lang

    # OCR 실행
    def runOCR(self):
        from PIL import Image
        try:
            img = Image.open(self.imagePath)
            self.resultText = pytesseract.image_to_string(img, lang=self.language)
            return True
        except Exception as e:
            print(f"[OCRProcessor] OCR 오류 발생: {e}")
            self.resultText = ""
            return False

    # OCR 결과 반환
    def getText(self):
        return self.resultText