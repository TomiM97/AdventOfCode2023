from typing import Any


class D2:
    def __init__(self):
        self.maxred = 12
        self.maxgreen = 13
        self.maxblue = 14
        self.IDsum = 0
    
    def readfile(self):
        file = open("AdventofCode2023/D2input1.txt","r")
        line = file.readline()
        while len(line) != 0:
            templine = line.lstrip("Game ")
            templine = templine.rsplit(": ")
            ID = int(templine[0])
            templine[1] = templine[1].rstrip("\n")
            sets = templine[1].rsplit("; ")
            for set in sets:
                result = self.checkset(set)
                if result == False:
                    break
            if result == True:
                self.IDsum += ID
            line = file.readline()
        file.close() 
        return self.IDsum
    
    def checkset(self, set: str):
        subsets = set.rsplit(", ")
        for subset in subsets:
            temp = subset.rsplit(" ")
            amount = int(temp[0])
            color = temp[1]
            if color == "red":
                if amount > self.maxred:
                    return False
            if color == "blue":
                if amount > self.maxblue:
                    return False
            if color == "green":
                if amount > self.maxgreen:
                    return False
        return True
        


if __name__ == "__main__":
    d2 = D2()
    print(d2.readfile())