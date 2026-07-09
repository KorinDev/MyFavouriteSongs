# so like yeah, this script uh, converts my CSV file into a fancy dancy nancy shmancy README.md file. cuz yeahhh. i guess.

README = """
This file contains a list of my favourite music in a nice, human readable format!
# My Favourite Music
---

|ID|NAME|AUTHOR|GENRE|
|---|---|---|---|
"""

with open("songs.csv", "r") as f:
    csv_file = f.readlines()


for line in csv_file:
    if line.startswith("id"):
        continue
    id,name,author,genre = line.strip().split(",")
    README += f"|{id}|**{name}**|{author}|{genre}|\n"



print(README)

with open("README.md", "w") as rf:
    rf.write(README)
