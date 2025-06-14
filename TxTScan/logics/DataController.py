from logics.TextProcessor import TextProcessor
from logics.ResultManager import ResultManager
from logics.OCRProcessor import OCRProcessor
from logics.Summarizer import Summarizer
from logics.Translator import Translator

# 프로그램의 데이터 처리
class DataController:
    def __init__(self, user):
        self.user = user  # 로그인된 사용자
        self.textProcessor = TextProcessor(OCRProcessor(), Summarizer(maxLen=150), Translator("ko")) # default 언어 : 한국어
        self.resultManager = ResultManager(user)

    # 텍스트의 요약/번역 처리
    def process(self, text):
        summary = self.textProcessor.processSummary(text)
        translation = self.textProcessor.processTranslate(summary)
        return translation

    # 결과 저장
    def saveResult(self, resultText):
        self.resultManager.saveResult(resultText)

    # 결과 목록 불러오기
    def getResultList(self):
        return self.resultManager.getResultList()

    # 저장된 상세 결과 불러오기
    def getResult(self, idx):
        return self.resultManager.getResult(idx)

    # 결과 삭제
    def deleteResult(self, idx):
        return self.resultManager.deleteResult(idx)

    # 이미지 처리
    def processOCR(self, imgPath):
        return self.textProcessor.processOCR(imgPath)