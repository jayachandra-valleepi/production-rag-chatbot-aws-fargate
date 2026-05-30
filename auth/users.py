users = {
    "jay": "1234",
    "admin": "admin",
    "Boss":"5678",
    "Yash": "4444"
}


def check_user(username: str, password: str):

    if username in users and users[username] == password:
        return True

    return False