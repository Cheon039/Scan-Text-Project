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

        tesseractCmd = shutil.which("tesseract")

        if not tesseractCmd:
            defaultPath = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
            if os.path.exists(defaultPath):
                tesseractCmd = defaultPath

        configPath = "config.json"
        if tesseractCmd:
            try:
                with open(configPath, "w") as f:
                    json.dump({"tesseract_path": tesseractCmd}, f, indent=2)
            except Exception as e:
                print(f"[OCRProcessor] config 생성 실패: {e}")

        if not tesseractCmd or not os.path.exists(tesseractCmd):
            raise FileNotFoundError("Tesseract 실행 파일을 찾을 수 없습니다. 시스템 PATH 또는 config.json을 확인하세요.")

        pytesseract.pytesseract.tesseract_cmd = tesseractCmd

    def setImagePath(self, path):
        self.imagePath = path

    def setLanguage(self, lang):
        self.language = lang

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

    def getText(self):
        return self.resultText