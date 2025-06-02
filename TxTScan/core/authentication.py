class Authentication:
    def __init__(self):
        # 임시 사용자 정보 (ID: user, PW: 1234)
        self.users = {"user": "12334"}

    def login(self, user_id: str, password: str) -> bool:
        return self.users.get(user_id) == password