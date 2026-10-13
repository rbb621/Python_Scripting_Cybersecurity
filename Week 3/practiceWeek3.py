from pathlib import Path

target_dir = Path("./data_folder")

for item in target_dir.iterdir():
    # Write the if-condition here
    if item.isfile() and item.suffix() == '.csv':
        print(item.name)

#Drill 1: Identifying Directories vs. Files
# You want to loop through a directory using pathlib 
# and print only the filenames (not subdirectories)
# that end with .csv.

#Fill in the missing line:


import shutil