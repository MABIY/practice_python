from pathlib import Path
import json


def get_favorite_number(path):
    favorite_number = input("your favorite number?")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    return favorite_number


def favorite_number():
    path = Path('favorite_number.json')
    favorite_number = get_stored_favorite_number(path)
    if favorite_number:
        print(f"your favorite_number:{favorite_number}")
    else:
        favorite_number = get_favorite_number(path)
        print(f"l will remember your favorite number ,when you next back!")


def get_stored_favorite_number(path):
    if path.exists():
        favorite_number = path.read_text()
        if not favorite_number:
            return None
        return json.loads(favorite_number)
    else:
        return None



favorite_number()
