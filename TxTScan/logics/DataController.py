from logics.TextProcessor import TextProcessor
from logics.ResultManager import ResultManager
from logics.OCRProcessor import OCRProcessor
from logics.Summarizer import Summarizer
from logics.Translator import Translator

class DataController:
    def __init__(self, user):
        self.user = user  # 로그인된 사용자
        self.textProcessor = TextProcessor(OCRProcessor(), Summarizer(maxLen=150), Translator("ko")) # default 언어 : 한국어
        self.resultManager = ResultManager(user)

    def process(self, text):
        summary = self.textProcessor.processSummary(text)
        translation = self.textProcessor.processTranslate(summary)
        return translation

    def saveResult(self, resultText):
        self.resultManager.saveResult(resultText)

    def getResultList(self):
        return self.resultManager.getResultList()

    def getResult(self, idx):
        return self.resultManager.getResult(idx)

    def deleteResult(self, idx):
        return self.resultManager.deleteResult(idx)

    def processOCR(self, imgPath):
        return self.textProcessor.processOCR(imgPath)