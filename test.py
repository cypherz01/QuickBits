def CreateFile():
    try:
        open("testFile.txt", "x")
    finally:
        return 0

CreateFile()    