
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class Summarizer:
    def __init__(self, maxLen=150):
        self.inputText = ""
        self.programResult = ""
        self.maxLen = maxLen
        self.summaryModel = None
        self.tokenizer = None

    def setInput(self, text):
        self.inputText = text

    def setModel(self):
        """
        사전 훈련된 요약 모델과 토크나이저 불러오기
        - huggingface.co에서 원하는 모델로 교체 가능
        """
        model_name = "facebook/bart-base"  # or "sshleifer/distilbart-cnn-12-6"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.summaryModel = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def runProgram(self):
        """요약 실행"""
        if not self.summaryModel or not self.tokenizer:
            return False
        if not self.inputText:
            return False

        try:
            inputs = self.tokenizer.encode(
                self.inputText, return_tensors="pt", max_length=1024, truncation=True
            )
            summary_ids = self.summaryModel.generate(
                inputs, max_length=self.maxLen, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True
            )
            self.programResult = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            return True
        except Exception as e:
            print(f"요약 오류: {e}")
            self.programResult = ""
            return False

    def getResult(self):
        return self.programResult