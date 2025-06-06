import json
import os

class Authentication:
    def __init__(self, filepath="TxTScan/userdata/userCredential.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

        # 초기화
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump({}, f)

    def register(self, user, pw):
        """사용자 등록 (중복 ID 불가)"""
        with open(self.filepath, "r") as f:
            data = json.load(f)

        if user in data:
            return False # 중복 ID
        
        data[user] = pw # ID: PW 저장
        with open(self.filepath, "w") as f:
            json.dump(data, f)
        return True
    
    def verify(self, user, pw):
        """로그인 인증"""
        with open(self.filepath, "r") as f:
            data = json.load(f)

        return user in data and data[user] == pw
