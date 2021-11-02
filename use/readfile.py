from os import error


import sys


def read(file_name):
    d = []
    try:
        with open(file_name) as f:
            line = f.readline()
            while line:
                line = d.append(int(line))
                line = f.readline()
        f.close()
    except FileNotFoundError as fnfe:
        print("Error: File not found ({}) on your PC.".format(file_name))
        error = True
    finally:
        if not error:
            return d


data = read("readfile.txt")
print(data)
