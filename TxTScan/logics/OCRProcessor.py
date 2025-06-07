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

        # 자동 경로 감지
        tesseract_cmd = shutil.which("tesseract")

        if not tesseract_cmd:
            # 기본 설치 위치 시도
            default_path = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
            if os.path.exists(default_path):
                tesseract_cmd = default_path

        # config.json 자동 생성
        config_path = "config.json"
        if tesseract_cmd:
            try:
                with open(config_path, "w") as f:
                    json.dump({"tesseract_path": tesseract_cmd}, f, indent=2)
                    print(f"[OCRProcessor] config.json 자동 생성 완료: {tesseract_cmd}")
            except Exception as e:
                print(f"[OCRProcessor] config 생성 실패: {e}")

        # 최종 확인
        if not tesseract_cmd or not os.path.exists(tesseract_cmd):
            raise FileNotFoundError("Tesseract 실행 파일을 찾을 수 없습니다. 시스템 PATH 또는 config.json을 확인하세요.")

        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd