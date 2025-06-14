import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langdetect import detect  # pip install langdetect

class Summarizer:
    def __init__(self, maxLen=100):
        self.maxLen = maxLen
        # 한국어 요약 모델
        self.ko_tokenizer = AutoTokenizer.from_pretrained("digit82/kobart-summarization")
        self.ko_model = AutoModelForSeq2SeqLM.from_pretrained("digit82/kobart-summarization")
        # 영어 요약 모델
        self.en_tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.en_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

        self.inputText = ""
        self.programResult = ""

    # 입력 테스트 세팅
    def setInput(self, text):
        self.inputText = text.strip()

    # 요약 실행
    def runProgram(self):
        try:
            lang = detect(self.inputText[:500])

            if lang == "ko":
                tokenizer, model = self.ko_tokenizer, self.ko_model
            else:
                tokenizer, model = self.en_tokenizer, self.en_model

            # 토큰화 및 모델 인퍼런스 수행
            # 읽을 수 있는 문장 -> 모델이 읽을 숫자 리스트 -> 요약문
            tokens = tokenizer(self.inputText, return_tensors="pt", truncation=True, max_length=1024)["input_ids"]

            output = model.generate(tokens, max_length=300, min_length=100, num_beams=4, early_stopping=True)

            summary = tokenizer.decode(output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True).strip()

            self.programResult = self.postProcess(summary)
            return True

        except Exception as e:
            print(f"요약 오류 : {e}")
            self.programResult = "[요약 실패: 요약 중 오류 발생]"
            return False

    # 요약 결과 후처리
    def postProcess(self, text):
        text = re.sub(r"(않고\s+){2,}", "않고 ", text)
        text = re.sub(r"(다\.){2,}", "다.", text)

        sentences = re.split(r'(?<=[.。!?])\s+', text)
        seen = set()
        unique = []
        for s in sentences:
            norm = s.strip()
            if len(norm) > 10 and norm not in seen:
                seen.add(norm)
                unique.append(norm)

        return " ".join(unique)

    # 결과 반환
    def getResult(self):
        return self.programResult or "[요약 결과 없음]"