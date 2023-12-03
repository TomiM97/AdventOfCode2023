class D2:
    def __init__(self):
        self.power = []
    
    def readfile(self):
        file = open("AdventofCode2023/D2input1.txt","r")
        line = file.readline()
        while len(line) != 0:
            templine = line.lstrip("Game ")
            templine = templine.rsplit(": ")
            templine[1] = templine[1].rstrip("\n")
            sets = templine[1].rsplit("; ")
            RGBminvalues = [0, 0, 0]
            for set in sets:
                tempRGBminvalues = self.checkset(set)
                if RGBminvalues[0] < tempRGBminvalues[0]:
                    RGBminvalues[0] = tempRGBminvalues[0]
                if RGBminvalues[1] < tempRGBminvalues[1]:
                    RGBminvalues[1] = tempRGBminvalues[1]
                if RGBminvalues[2] < tempRGBminvalues[2]:
                    RGBminvalues[2] = tempRGBminvalues[2]
            print(RGBminvalues)
            # multiply RGBminvalues with each other and add to list
            self.power.append(RGBminvalues[0] * RGBminvalues[1] * RGBminvalues[2])
            line = file.readline()
        # sum them to get the final result
        print(self.power)
        result = sum(self.power)
        file.close() 
        return result
    
    def checkset(self, set: str):
        subsets = set.rsplit(", ")
        RGBminvalues = [0, 0, 0]
        for subset in subsets:
            temp = subset.rsplit(" ")
            cubes = Cubes(int(temp[0]), temp[1])
            if cubes.color == "red":
                if cubes.amount > RGBminvalues[0]:
                    RGBminvalues[0] = cubes.amount
            if cubes.color == "green":
                if cubes.amount > RGBminvalues[1]:
                    RGBminvalues[1] = cubes.amount
            if cubes.color == "blue":
                if cubes.amount > RGBminvalues[2]:
                    RGBminvalues[2] = cubes.amount
        # multiply RGBminvalues with each other and add to list
        RGBminvalues = [RGBminvalues[0], RGBminvalues[1], RGBminvalues[2]]
            
        return RGBminvalues
        
class Cubes:
    def __init__(self, amount: int, color: str):
        self.amount = amount
        self.color = color

    def getAmount(self):
        return self.amount

    def getColor(self):
        return self.color


if __name__ == "__main__":
    d2 = D2()
    print(d2.readfile())