import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Summarizer:
    def __init__(self, maxLen=100):
        self.maxLen = maxLen
        model_name = "digit82/kobart-summarization"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.inputText = ""
        self.programResult = ""

    def setInput(self, text):
        self.inputText = text.strip()

    def setModel(self):
        pass  # 이미 __init__에서 설정 완료

    def runProgram(self):
        try:
            # 1. 전체 입력을 tokenizer로 인코딩 (토큰 기준 1024 제한)
            tokens = self.tokenizer(
                self.inputText,
                return_tensors="pt",
                truncation=True,
                max_length=1024
            )["input_ids"]

            # 2. 요약 실행
            output = self.model.generate(
                tokens,
                max_length=300,
                min_length=100,
                num_beams=4,
                early_stopping=True
            )

            summary = self.tokenizer.decode(
                output[0],
                skip_special_tokens=True,
                clean_up_tokenization_spaces=True
            ).strip()

            # 3. 후처리
            self.programResult = self.postProcess(summary)
            return True

        except Exception as e:
            print(f"[Summarizer 오류] {e}")
            self.programResult = "[요약 실패: Summarizer 오류 발생]"
            return False

    def postProcess(self, text):
        """후처리: 반복 제거, 문장 정리 등"""

        # 불필요 반복 단어 제거
        text = re.sub(r"(않고\s+){2,}", "않고 ", text)
        text = re.sub(r"(다\.){2,}", "다.", text)

        # 문장 단위 중복 제거
        sentences = re.split(r'(?<=[.。!?])\s+', text)
        seen = set()
        unique = []
        for s in sentences:
            norm = s.strip()
            if len(norm) > 10 and norm not in seen:
                seen.add(norm)
                unique.append(norm)

        return " ".join(unique)

    def getResult(self):
        return self.programResult or "[요약 결과 없음]"