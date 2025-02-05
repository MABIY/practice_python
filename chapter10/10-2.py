from pathlib import Path

print("--- Reading in the entire file:")
path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python','C')
    print(line)