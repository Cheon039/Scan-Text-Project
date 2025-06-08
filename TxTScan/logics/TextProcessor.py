class TextProcessor:
    def __init__(self, ocrProcessor, summarizer, translator):
        self.ocr = ocrProcessor
        self.summarizer = summarizer
        self.translator = translator

    def processOCR(self, imagePath):
        """이미지 경로를 받아 OCR 수행 → 텍스트 추출"""
        self.ocr.setImagePath(imagePath)
        self.ocr.setLanguage("kor")  # 기본 한국어
        if self.ocr.runOCR():
            return self.ocr.getText()
        return ""

    def processSummary(self, text):
        """텍스트를 요약하여 반환"""
        self.summarizer.setInput(text)
        self.summarizer.setModel()
        success = self.summarizer.runProgram()

        result = self.summarizer.getResult()
        if success and isinstance(result, str) and result.strip():
            return result
        else:
            print(f"[DEBUG] 요약 실패 또는 비정상 타입: {type(result)} / {repr(result)}")
            return "[요약 실패]"

    def processTranslate(self, text):
        """텍스트를 번역하여 반환"""
        result = self.translator.translate(text)
        if not isinstance(result, str):
            print(f"[ERROR] 번역 결과 타입 오류: {type(result)} → {result}")
            return "[번역 실패]"
        return result

    def process(self, text):
        summary = self.processSummary(text)
        print(f"[DEBUG] 요약 결과: {summary} ({type(summary)})")

        translated = self.processTranslate(summary)
        print(f"[DEBUG] 번역 결과: {translated} ({type(translated)})")

        return translated