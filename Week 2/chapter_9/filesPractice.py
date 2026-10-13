from pathlib import Path
import os
import stat

folder_path = Path('/Users/rickyberliant/Documents/Fall 2026/CYBV 312/Week 2/chapter_9')
file_name = 'testing.txt'

full_path = folder_path/file_name

print(full_path)


# Drill 2 — Multiple Files

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for file in myFiles:
    print(Path(folder_path / file))

# Drill 3 — Getting User Input

directoryInput = input('Enter a directory: ')

user_path = Path(directoryInput)
print(user_path)

# Drill 4 — Exploring a Directory
p = Path(directoryInput)
for subdir in p.iterdir():
    if subdir.is_file():
        print(subdir)


# Drill 5 — Print the Full Filepath

pathMap = Path(directoryInput)
for entry in pathMap.iterdir():
    print(entry)

# Drill #6 — os.stat() and file size.

fileInput = input('Enter a file: ')
fileSize = Path(fileInput)

print('File Size: ', fileSize.stat().st_size)