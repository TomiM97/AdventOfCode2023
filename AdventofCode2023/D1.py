def sumnro():
    file = open("AdventofCode2023/D1input2.txt","r")
    summa = 0
    line = file.readline()
    while len(line) != 0:
        
        firstnro = float("inf")
        tempnro = float("inf")
        for i in range(len(line)):
            if firstnro != float("inf"):
                if line[i:i+3] == "one":
                    tempnro = "1"
                if line[i:i+3] == "two":
                    tempnro = "2"
                if line[i:i+5] == "three":
                    tempnro = "3"
                if line[i:i+4] == "four":
                    tempnro = "4"
                if line[i:i+4] == "five":
                    tempnro = "5"
                if line[i:i+3] == "six":
                    tempnro = "6"
                if line[i:i+5] == "seven":
                    tempnro = "7"
                if line[i:i+5] == "eight":
                    tempnro = "8"
                if line[i:i+4] == "nine":
                    tempnro = "9"
                if line[i].isdigit():
                    tempnro = line[i]
            if firstnro == float("inf"):
                if line[i:i+3] == "one":
                    firstnro = "1"
                    tempnro = firstnro
                if line[i:i+3] == "two":
                    firstnro = "2"
                    tempnro = firstnro
                if line[i:i+5] == "three":
                    firstnro = "3"
                    tempnro = firstnro
                if line[i:i+4] == "four":
                    firstnro = "4"
                    tempnro = firstnro
                if line[i:i+4] == "five":
                    firstnro = "5"
                    tempnro = firstnro
                if line[i:i+3] == "six":
                    firstnro = "6"
                    tempnro = firstnro
                if line[i:i+5] == "seven":
                    firstnro = "7"
                    tempnro = firstnro
                if line[i:i+5] == "eight":
                    firstnro = "8"
                    tempnro = firstnro
                if line[i:i+4] == "nine":
                    firstnro = "9"
                    tempnro = firstnro
                if line[i].isdigit():
                    firstnro = line[i]
                    tempnro = firstnro
                

        two_digit_nro = int(firstnro + tempnro)
        summa = summa + two_digit_nro
        line = file.readline()
        print(f"{two_digit_nro} and {summa}")
    
    file.close()
    return summa


if __name__ == "__main__":
    print(sumnro())