f = open("file.txt", "wt")
f.write("MYSECRETINFO")
f.close()

with open("file.bin", "wt") as f: # открываем файл с помощью with
    f.write("kokq1")


with open("file.bin", "wt") as f: # открываем файл с помощью with
    f.write("kok1221")