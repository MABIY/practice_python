from pathlib import Path
import json


def get_stored_username(path):
    """如果存储了用户名,就获取它"""
    if path.exists():
        contents = path.read_text()
        if not contents:
            return None
        return json.loads(contents)
    else:
        return None
def get_new_username(path):
    """提示用户输入用户名"""
    username = input("What is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    path = Path('username1.json')
    username = get_stored_username(path)
    if check_username(username):
        print(f"Welcome back, {username}!")
        return

    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")

def check_username(username):
    correct = input(f"Are you {username}? (y/n)")
    if correct == 'y':
        return True
    return False

greet_user()