class TextProcessor:
    def __init__(self, ocrProcessor, summarizer, translator):
        self.ocr = ocrProcessor
        self.summarizer = summarizer
        self.translator = translator

    def processOCR(self, imgPath):
        self.ocr.setImagePath(imgPath)
        self.ocr.setLanguage("kor")  # 기본 한국어
        if self.ocr.runOCR():
            return self.ocr.getText()
        return ""

    def processSummary(self, text):
        self.summarizer.setInput(text)
        self.summarizer.setModel()
        success = self.summarizer.runProgram()

        result = self.summarizer.getResult()
        if success and isinstance(result, str) and result.strip():
            return result
        else:
            #print(f"요약 실패 또는 타입 오류: {type(result)} / {repr(result)}")
            return "[요약 실패]"

    def processTranslate(self, text):
        result = self.translator.translate(text)
        if not isinstance(result, str):
            #print(f"번역 결과 타입 오류: {type(result)} → {result}")
            return "[번역 실패]"
        return result

    def process(self, text):
        summary = self.processSummary(text)
        #print(f"요약 결과: {summary} ({type(summary)})")

        translate = self.processTranslate(summary)
        #print(f"번역 결과: {translate} ({type(translate)})")

        return translate