class TextProcessor:
    def __init__(self, ocrProcessor, summarizer, translator):
        self.ocr = ocrProcessor
        self.summarizer = summarizer
        self.translator = translator

    # OCR 실행
    def processOCR(self, imgPath):
        self.ocr.setImagePath(imgPath)
        self.ocr.setLanguage("kor")  # 기본 한국어
        if self.ocr.runOCR():
            return self.ocr.getText()
        return ""

    # 요약 시작
    def processSummary(self, text):
        self.summarizer.setInput(text)
        success = self.summarizer.runProgram()

        result = self.summarizer.getResult()
        if success and isinstance(result, str) and result.strip():
            return result
        else:
            #print(f"요약 실패 또는 타입 오류: {type(result)} / {repr(result)}")
            return "[요약 실패]"

    # 번역 시작
    def processTranslate(self, text):
        result = self.translator.translate(text)
        if not isinstance(result, str):
            #print(f"번역 결과 타입 오류: {type(result)} → {result}")
            return "[번역 실패]"
        return result

    # 전체를 통합으로 처리 (요약 → 번역)
    def process(self, text):
        summary = self.processSummary(text)
        #print(f"요약 결과: {summary} ({type(summary)})")

        translate = self.processTranslate(summary)
        #print(f"번역 결과: {translate} ({type(translate)})")

        return translate