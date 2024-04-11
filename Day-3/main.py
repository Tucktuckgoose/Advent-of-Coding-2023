import re

def part1():
    # Find all part numbers in file and save them to dict objects referencing lines
    partNumDict = {} # This dictionary will hold the part numbers line by line
    partIndexDict = {} # This dictionary will hold the string index number for each entry in the partNumDict
    symbolDict = {} # This dictionary will hold the symbols on each line, line by line
    symbolIndexDict = {} # This dictionary will hold the symbol index number for each entry in the symbolDict
    numLines = 0 # This is the number of lines in the input file

    with open('input.txt') as file:
        i = 0

        # This for loop is where we populate the parts number dictionary and the parts starting indices dictionary
        for line in file:
            splitLine = re.split(r'\D+',line)

            # Find the part numbers in each line, put them into a list, then put that list into the partNumDict dictionary
            partList = []
            for anEntry in splitLine:
                if not anEntry == "" and anEntry.isnumeric():
                    partList.append(anEntry)
            partNumDict[i] = partList

            # Now find the indices of the part numbers in each line, put them into a list, then put that list into the partIndexDict
            tmpStart = 0
            indexList = []
            for anEntry in partList:
                anIndex = line.find(anEntry,tmpStart)
                if (anIndex < 0):
                    raise ValueError('The part number cannot be found in the string, bad code')
                else:
                    indexList.append(anIndex)
                    tmpStart = anIndex + len(anEntry)
            partIndexDict[i] = indexList
            numLines = i + 1
            i += 1
    
    with open('input.txt') as file:
        i = 0 

        for line in file:

            # Find the special characters in each line, put them into a list, then put that list into the symbolDict dictionary
            symbolList = []
            for aChar in line:
                if not aChar == "." and not aChar == "\n" and not aChar.isnumeric():
                    symbolList.append(aChar)
            symbolDict[i] = symbolList

            # Now find the indices of the symbols in each line, put them into a list, then put that list into the symbolIndexDict            
            tmpStart = 0
            indexList = []
            for anEntry in symbolList:
                anIndex = line.find(anEntry,tmpStart)
                if (anIndex < 0):
                    raise ValueError('The symbol cannot be found in the string, bad code')
                else:
                    indexList.append(anIndex)
                    tmpStart = anIndex + 1
            symbolIndexDict[i] = indexList
            i += 1

    # Look through each entry in the special symbol index dictionary, check the lines above, even, and below to see if there is an entry next to that special symbol
    # If there is one, then remove it from the part dictionary and index dictionary and add it to the sum
    partNumSum = 0
    for i in range(numLines):
        for aSymbolIndex in symbolIndexDict[i]:
            for j in range(i-1, i+2):
                if j < 0 or j > numLines - 1:
                    continue
                k = 0
                listToRemove = []
                for aPartIndex in partIndexDict[j]:
                    tmpPartNumList = partNumDict[j]
                    if ((aSymbolIndex + 1 >= aPartIndex) and (aSymbolIndex - 1 < aPartIndex + len(tmpPartNumList[k]))): # Might not need to have the equals signs - test
                        partNumSum += int(tmpPartNumList[k])
                        listToRemove.append(k)
                    k += 1

                tmpPartNumList = partNumDict[j].copy()
                tmpPartIndexList = partIndexDict[j].copy()
                for anEntry in reversed(listToRemove):
                    tmpPartNumList.pop(anEntry)
                    tmpPartIndexList.pop(anEntry)

                partNumDict[j] = tmpPartNumList
                partIndexDict[j] = tmpPartIndexList

    
    print(partNumSum)

def part2():
    # Find all part numbers in file and save them to dict objects referencing lines
    partNumDict = {} # This dictionary will hold the part numbers line by line
    partIndexDict = {} # This dictionary will hold the string index number for each entry in the partNumDict
    symbolDict = {} # This dictionary will hold the symbols on each line, line by line
    symbolIndexDict = {} # This dictionary will hold the symbol index number for each entry in the symbolDict
    numLines = 0 # This is the number of lines in the input file

    with open('input.txt') as file:
        i = 0

        # This for loop is where we populate the parts number dictionary and the parts starting indices dictionary
        for line in file:
            splitLine = re.split(r'\D+',line)

            # Find the part numbers in each line, put them into a list, then put that list into the partNumDict dictionary
            partList = []
            for anEntry in splitLine:
                if not anEntry == "" and anEntry.isnumeric():
                    partList.append(anEntry)
            partNumDict[i] = partList

            # Now find the indices of the part numbers in each line, put them into a list, then put that list into the partIndexDict
            tmpStart = 0
            indexList = []
            for anEntry in partList:
                anIndex = line.find(anEntry,tmpStart)
                if (anIndex < 0):
                    raise ValueError('The part number cannot be found in the string, bad code')
                else:
                    indexList.append(anIndex)
                    tmpStart = anIndex + len(anEntry)
            partIndexDict[i] = indexList
            numLines = i + 1
            i += 1
    
    with open('input.txt') as file:
        i = 0 

        for line in file:

            # Find the special characters in each line, put them into a list, then put that list into the symbolDict dictionary
            symbolList = []
            for aChar in line:
                if not aChar == "." and not aChar == "\n" and not aChar.isnumeric():
                    symbolList.append(aChar)
            symbolDict[i] = symbolList

            # Now find the indices of the symbols in each line, put them into a list, then put that list into the symbolIndexDict            
            tmpStart = 0
            indexList = []
            for anEntry in symbolList:
                anIndex = line.find(anEntry,tmpStart)
                if (anIndex < 0):
                    raise ValueError('The symbol cannot be found in the string, bad code')
                else:
                    indexList.append(anIndex)
                    tmpStart = anIndex + 1
            symbolIndexDict[i] = indexList
            i += 1

    # Look through each entry in the special symbol index dictionary, find the ones that are "*" characters, and determine if there are two part numbers next to it - if so multiply those together
    gearRatioSum = 0
    for i in range(numLines):
        tmpSymbolDict = symbolDict[i].copy()
        m = 0
        for aSymbolIndex in symbolIndexDict[i]:
            if (tmpSymbolDict[m] == "*"):
                gearList = []
                for j in range(i-1, i+2):
                    if j < 0 or j > numLines - 1:
                        continue
                    k = 0
                    for aPartIndex in partIndexDict[j]:
                        tmpPartNumList = partNumDict[j]
                        if ((aSymbolIndex + 1 >= aPartIndex) and (aSymbolIndex - 1 < aPartIndex + len(tmpPartNumList[k]))):
                            gearList.append(int(tmpPartNumList[k]))
                        k += 1
                if (len(gearList) > 1):
                    # This is a gear
                    gearProduct = gearList[0] * gearList[1]
                    gearRatioSum += gearProduct
            m += 1

    
    print(gearRatioSum)

if __name__ == "__main__":
    #part1()
    part2()