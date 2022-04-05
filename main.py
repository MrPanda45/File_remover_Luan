import os

# HERE YOU'LL WRITE THE DIRECTORY THE FILES CURRENTLY ARE (BETWEEN THE "" AND, IN CASE OF USING "\", USE 2 INSTEAD
# OF ONLY 1: "\\" LIKE SO)
DIRECTORY = ""

EXTENSIONS = [".mkv", ",mp4", ".asf", ".avi", ".m4v", ".mov", ".mpg", ".mpeg", ".wmv"]

for file in os.listdir(DIRECTORY):

    size = os.path.getsize(f"{DIRECTORY}\\{file}")
    if size < 1000000:
        os.remove(f"{DIRECTORY}\\{file}")

    file_name = os.path.splitext(file)[1]

    if file_name not in EXTENSIONS:
        try:
            os.remove(f"{DIRECTORY}/{file}")
        except OSError:
            print("Arquivo não encontrado")
            pass


