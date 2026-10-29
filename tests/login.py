# tests/login.py
# 간단한 로그인 기# tests/login.py
# 간단한 로그인 기능 예제

USERS = {
    "admin": "1234",
    "student": "cwnu2026",
}


def login(username, password):
    """아이디와 비밀번호가 맞으면 True를 반환"""
    if username not in USERS:
        print("존재하지 않는 사용자입니다.")
        return False

    if USERS[username] != password:
        print("비밀번호가 틀렸습니다.")
        return False

    print(f"{username}님, 환영합니다!")
    return True


if __name__ == "__main__":
    login("admin", "1234")
    login("student", "wrong")# tests/login.py
