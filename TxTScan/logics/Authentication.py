import json
import os

# 사용자 정보 저장 클래스
class Authentication:
    def __init__(self, filepath="TxTScan/userdata/userCredential.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

        # 초기파일 생성
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump({}, f)

    # 회원가입 기능 (중복이 불가능 하도록)
    def register(self, user, pw):
        with open(self.filepath, "r") as f:
            data = json.load(f)

        if user in data:
            return False # ID 중복 시
        
        data[user] = pw # ID: PW 저장
        with open(self.filepath, "w") as f:
            json.dump(data, f)
        return True
    
    # 로그인 인증
    def verify(self, user, pw):
        with open(self.filepath, "r") as f:
            data = json.load(f)

        return user in data and data[user] == pw
