from pathlib import Path
import json

def greet_user():
    """问候用户，并指出其名字"""
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        if not contents:
            return False
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
        return True
    else:
        return False
greet_succeeded = greet_user()
if not greet_succeeded:
    username= input("What is your name?")
    contents = json.dumps(username)
    path = Path('username.json')
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
