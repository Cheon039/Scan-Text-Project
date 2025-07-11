import json
import os

class ResultManager:
    def __init__(self, user):
        self.user = user
        self.filePath = f"TxTScan/userResult/results{user}.json"
        os.makedirs(os.path.dirname(self.filePath), exist_ok=True)

        # 파일이 없으면 빈 리스트로 초기화
        if not os.path.exists(self.filePath):
            with open(self.filePath, "w") as f:
                json.dump([], f)

    # 결과 저장
    def saveResult(self, resultText):
        with open(self.filePath, "r") as f:
            data = json.load(f)

        data.insert(0, resultText)  # 최신 결과를 맨 위에 추가
        with open(self.filePath, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # 결과 목록을 반환
    def getResultList(self):
        with open(self.filePath, "r") as f:
            data = json.load(f)

        # 결과 첫 줄만 잘라내서 미리보기 리스트로 반환
        return [text.split('\n')[0][:50] + "..." if len(text) > 50 else text for text in data]

    # 특정 결과 보기
    def getResult(self, index):
        with open(self.filePath, "r") as f:
            data = json.load(f)

        if 0 <= index < len(data):
            return data[index]
        return "결과 없음"

    # 선택 결과 삭제
    def deleteResult(self, index):
        with open(self.filePath, "r") as f:
            data = json.load(f)

        if 0 <= index < len(data):
            del data[index]
            with open(self.filePath, "w") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        return False