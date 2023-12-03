def part1():
    trueRed = 12
    trueGreen = 13
    trueBlue = 14
    sum = 0
    with open('input.txt') as file:
        for line in file:
            splitLine = line.split(' ')
            for i in range(len(splitLine)):
                splitLine[i] = splitLine[i].replace(',','')
                splitLine[i] = splitLine[i].replace(';','')
                splitLine[i] = splitLine[i].replace(':','')
                splitLine[i] = splitLine[i].replace('\n','')
                
            fail = False
            for i in range(2,len(splitLine),2):
                # Test red
                if(splitLine[i+1] == 'red'):
                    if(int(splitLine[i]) > trueRed):
                        fail = True
                        break
            
                # Test green
                if(splitLine[i+1] == 'green'):
                    if(int(splitLine[i]) > trueGreen):
                        fail = True
                        break

                # Test blue
                if(splitLine[i+1] == 'blue'):
                    if(int(splitLine[i]) > trueBlue):
                        fail = True
                        break

            if(not fail):
                sum += int(splitLine[1])

        print(sum)

def part2():
    sum = 0
    with open('input.txt') as file:
        for line in file:
            splitLine = line.split(' ')
            for i in range(len(splitLine)):
                splitLine[i] = splitLine[i].replace(',','')
                splitLine[i] = splitLine[i].replace(';','')
                splitLine[i] = splitLine[i].replace(':','')
                splitLine[i] = splitLine[i].replace('\n','')

            minRed = 0
            minGreen = 0
            minBlue = 0
                
            for i in range(2,len(splitLine),2):
                # Test red
                if(splitLine[i+1] == 'red'):
                    if(int(splitLine[i]) > minRed):
                        minRed = int(splitLine[i])

                # Test green
                if(splitLine[i+1] == 'green'):
                    if(int(splitLine[i]) > minGreen):
                        minGreen = int(splitLine[i])

                # Test blue
                if(splitLine[i+1] == 'blue'):
                    if(int(splitLine[i]) > minBlue):
                        minBlue = int(splitLine[i])
            
            myProduct = minRed * minGreen * minBlue
            sum += myProduct
        print(sum)

if __name__ == "__main__":
    part1()
    part2()