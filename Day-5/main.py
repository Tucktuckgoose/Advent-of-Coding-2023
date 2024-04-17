def mapInput(aDict, aDestStart, aSourceStart, aRangeLength):
    for i in range(aRangeLength):
        aDict[aSourceStart + i] = aDestStart + i

def getHighestKey(aDict):
    if (len(aDict) > 0):
        return max(k for k, v in aDict.items())
    else:
        return 0

def getHighestValue(aDict):
    if (len(aDict) > 0):
        return max(v for k, v in aDict.items())
    else:
        return 0

def setMapDefaults(aDict, aMax):
    for i in range(aMax + 1):
        aDict[i] = aDict.get(i,i)

def part1():
    with open ('input.txt') as file:
        seeds = []
        seed2soil = {}
        soil2fert = {}
        fert2watr = {}
        watr2ligt = {}
        ligt2temp = {}
        temp2humd = {}
        humd2locn = {}
        listOfDicts = [seed2soil, soil2fert, fert2watr, watr2ligt, ligt2temp, temp2humd, humd2locn]
        inputSection = "seeds"
        for line in file:
            match inputSection:
                case "seeds":
                    # Create list of seeds
                    seeds = map(int, line.split()[1:])
                    inputSection = "skip"
                case "skip":
                    inputSection = "seed2soil"
                case "seed2soil":
                    # Create seed to soil map
                    if line.strip() == "seed-to-soil map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "soil2fert"
                    else:
                        destStart, sourceStart, rangeLength = map(int,line.split())
                        mapInput(seed2soil, destStart, sourceStart, rangeLength)
                case "soil2fert":
                    # Create soil to fertilizer map
                    if line.strip() == "soil-to-fertilizer map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "fert2watr"
                    else:
                        destStart, sourceStart, rangeLength = map(int,line.split())
                        mapInput(soil2fert, destStart, sourceStart, rangeLength)
                case "fert2watr":
                    # Create fertilizer to water map
                    if line.strip() == "fertilizer-to-water map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "watr2ligt"
                    else:
                        destStart, sourceStart, rangeLength = map(int,line.split())
                        mapInput(fert2watr, destStart, sourceStart, rangeLength)
                case "watr2ligt":
                    # Create water to light map
                    if line.strip() == "water-to-light map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "ligt2temp"
                    else:
                        destStart, sourceStart, rangeLength = map(int,line.split())
                        mapInput(watr2ligt, destStart, sourceStart, rangeLength)
                case "ligt2temp":
                    # Create light to temperature map
                    if line.strip() == "light-to-temperature map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "temp2humd"
                    else:
                        destStart, sourceStart, rangeLength = map(int,line.split())
                        mapInput(ligt2temp, destStart, sourceStart, rangeLength)
                case "temp2humd":
                    # Create temperature to humidity map
                    if line.strip() == "temperature-to-humidity map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "humd2locn"
                    else:
                        destStart, sourceStart, rangeLength = map(int,line.split())
                        mapInput(temp2humd, destStart, sourceStart, rangeLength)
                case "humd2locn":
                    # Create humidity to location map
                    if line.strip() == "humidity-to-location map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "skip"
                    else:
                        destStart, sourceStart, rangeLength = map(int,line.split())
                        mapInput(humd2locn, destStart, sourceStart, rangeLength)
                case _:
                    pass
        maxNumber = 0
        for aDict in listOfDicts:
            aMaxKey = getHighestKey(aDict)
            if (aMaxKey > maxNumber):
                maxNumber = aMaxKey
            aMaxValue = getHighestValue(aDict)
            if (aMaxValue > maxNumber):
                maxNumber = aMaxValue
        for aDict in listOfDicts:
            setMapDefaults(aDict, maxNumber)

        # Make jumps between every map and find the lowest location of all paths from seeds
        minLocation = maxNumber
        for seed in seeds:
            #print("Seed: ",seed)
            soil = seed2soil[seed]
            #print("Soil: ",soil)
            fert = soil2fert[soil]
            #print("Fertilizer: ", fert)
            water = fert2watr[fert]
            #print("Water: ", water)
            light = watr2ligt[water]
            #print("Light: ", light)
            temperature = ligt2temp[light]
            #print("Temperature: ", temperature)
            humidity = temp2humd[temperature]
            #print("Humidity: ", humidity)
            location = humd2locn[humidity]
            #print("Location: ", location, "\n")
            if (location < minLocation):
                minLocation = location
        
        print("Minimum Location: ", minLocation)

if __name__ == "__main__":
    part1()
    #part2()