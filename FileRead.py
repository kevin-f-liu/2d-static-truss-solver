import numpy

# Open file
class FileRead:
    def __init__(self, file):
        self.f = None;
        self.bridges = [];
        try:
            f = open(file)
        except FileNotFoundError:
            print("%s Not Found!" % file)
            f = None

        if f is not None:
            l = f.readline()
            while l != "":
                self.bridges.append(l)
                l = f.readline()

    def getBridges(self):
        return self.bridges

file = FileRead("bridges.txt")
print(file.getBridges())











