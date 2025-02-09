from pathlib import Path

from word_count import count_worlds

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_worlds(path)