import sys

def findOffset(aList: list[list[int]], aSource: int) -> int:
    for entry in aList:
        if aSource >= entry[1] and aSource <= (entry[1] + entry[2]):
            # This entry covers this source number, determine delta from source to destination
            delta: int = entry[0] - entry[1]
            return aSource + delta
    # Didn't find a relevant entry in the lists, no offset, return aSource as the destination
    return aSource

def findDest2SourceOffset(aList: list[list[int]], aDest: int) -> int:
    for entry in aList:
        if aDest >= entry[0] and aDest <= (entry[0] + entry[2]):
            # This entry covers this destination number, determine delta from source to destination
            delta: int = entry[1] - entry[0]
            return aDest + delta
    # Didn't find a relevant entry in the lists, no offset, return aDest as the source
    return aDest

def part1():
    with open ('input.txt') as file:
        seeds = []
        seed2soil = []
        soil2fert = []
        fert2watr = []
        watr2ligt = []
        ligt2temp = []
        temp2humd = []
        humd2locn = []
        listOfLists = [seed2soil, soil2fert, fert2watr, watr2ligt, ligt2temp, temp2humd, humd2locn]
        inputSection = "seeds"
        for line in file:
            match inputSection:
                case "seeds":
                    # Create list of seeds
                    seeds = [int(i) for i in line.split()[1:]]
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
                        entry: list[int] = [int(i) for i in line.split()]
                        seed2soil.append(entry)
                case "soil2fert":
                    # Create soil to fertilizer map
                    if line.strip() == "soil-to-fertilizer map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "fert2watr"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        soil2fert.append(entry)
                case "fert2watr":
                    # Create fertilizer to water map
                    if line.strip() == "fertilizer-to-water map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "watr2ligt"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        fert2watr.append(entry)
                case "watr2ligt":
                    # Create water to light map
                    if line.strip() == "water-to-light map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "ligt2temp"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        watr2ligt.append(entry)
                case "ligt2temp":
                    # Create light to temperature map
                    if line.strip() == "light-to-temperature map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "temp2humd"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        ligt2temp.append(entry)
                case "temp2humd":
                    # Create temperature to humidity map
                    if line.strip() == "temperature-to-humidity map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "humd2locn"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        temp2humd.append(entry)
                case "humd2locn":
                    # Create humidity to location map
                    if line.strip() == "humidity-to-location map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "skip"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        humd2locn.append(entry)
                case _:
                    pass

        # Make jumps between every map and find the lowest location of all paths from seeds
        minLocation = sys.maxsize
        for seed in seeds:
            #print("Seed: ",seed)
            soil = findOffset(seed2soil,seed)
            #print("Soil: ",soil)
            fert = findOffset(soil2fert,soil)
            #print("Fertilizer: ", fert)
            water = findOffset(fert2watr,fert)
            #print("Water: ", water)
            light = findOffset(watr2ligt,water)
            #print("Light: ", light)
            temperature = findOffset(ligt2temp,light)
            #print("Temperature: ", temperature)
            humidity = findOffset(temp2humd,temperature)
            #print("Humidity: ", humidity)
            location = findOffset(humd2locn,humidity)
            #print("Location: ", location, "\n")
            if (location < minLocation):
                minLocation = location
        
        print("Part 1 Minimum Location: ", minLocation)

def part2():
    with open ('input.txt') as file:
        seeds = []
        seed2soil = []
        soil2fert = []
        fert2watr = []
        watr2ligt = []
        ligt2temp = []
        temp2humd = []
        humd2locn = []
        listOfLists = [seed2soil, soil2fert, fert2watr, watr2ligt, ligt2temp, temp2humd, humd2locn]
        inputSection = "seeds"
        for line in file:
            match inputSection:
                case "seeds":
                    # Create list of seeds
                    seedsEntry = [int(i) for i in line.split()[1:]]
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
                        entry: list[int] = [int(i) for i in line.split()]
                        seed2soil.append(entry)
                case "soil2fert":
                    # Create soil to fertilizer map
                    if line.strip() == "soil-to-fertilizer map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "fert2watr"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        soil2fert.append(entry)
                case "fert2watr":
                    # Create fertilizer to water map
                    if line.strip() == "fertilizer-to-water map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "watr2ligt"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        fert2watr.append(entry)
                case "watr2ligt":
                    # Create water to light map
                    if line.strip() == "water-to-light map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "ligt2temp"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        watr2ligt.append(entry)
                case "ligt2temp":
                    # Create light to temperature map
                    if line.strip() == "light-to-temperature map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "temp2humd"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        ligt2temp.append(entry)
                case "temp2humd":
                    # Create temperature to humidity map
                    if line.strip() == "temperature-to-humidity map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "humd2locn"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        temp2humd.append(entry)
                case "humd2locn":
                    # Create humidity to location map
                    if line.strip() == "humidity-to-location map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "skip"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        humd2locn.append(entry)
                case _:
                    pass

        # Make jumps between every map and find the lowest location of all paths from seeds
        minLocation = sys.maxsize
        counter: int = 0
        seeds2eval: int = 0
        for i in range(0, len(seedsEntry), 2):
            seeds2eval += seedsEntry[i+1]
        for i in range(0, len(seedsEntry), 2):
            for j in range(seedsEntry[i+1]):
                #print("Seed: ",seed)
                soil = findOffset(seed2soil,seedsEntry[i]+j)
                #print("Soil: ",soil)
                fert = findOffset(soil2fert,soil)
                #print("Fertilizer: ", fert)
                water = findOffset(fert2watr,fert)
                #print("Water: ", water)
                light = findOffset(watr2ligt,water)
                #print("Light: ", light)
                temperature = findOffset(ligt2temp,light)
                #print("Temperature: ", temperature)
                humidity = findOffset(temp2humd,temperature)
                #print("Humidity: ", humidity)
                location = findOffset(humd2locn,humidity)
                #print("Location: ", location, "\n")
                if (location < minLocation):
                    minLocation = location
                counter += 1
                if (counter % 1000000 == 0):
                    print(f'Completed {counter} steps out of {seeds2eval} - {counter / seeds2eval * 100} percent complete')
        print("Part 2 Minimum Location: ", minLocation)

def part2Improved() -> None:
    with open ('input.txt') as file:
        seeds = []
        seed2soil = []
        soil2fert = []
        fert2watr = []
        watr2ligt = []
        ligt2temp = []
        temp2humd = []
        humd2locn = []
        listOfLists = [seed2soil, soil2fert, fert2watr, watr2ligt, ligt2temp, temp2humd, humd2locn]
        inputSection = "seeds"
        for line in file:
            match inputSection:
                case "seeds":
                    # Create list of seeds
                    seedsEntry = [int(i) for i in line.split()[1:]]
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
                        entry: list[int] = [int(i) for i in line.split()]
                        seed2soil.append(entry)
                case "soil2fert":
                    # Create soil to fertilizer map
                    if line.strip() == "soil-to-fertilizer map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "fert2watr"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        soil2fert.append(entry)
                case "fert2watr":
                    # Create fertilizer to water map
                    if line.strip() == "fertilizer-to-water map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "watr2ligt"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        fert2watr.append(entry)
                case "watr2ligt":
                    # Create water to light map
                    if line.strip() == "water-to-light map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "ligt2temp"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        watr2ligt.append(entry)
                case "ligt2temp":
                    # Create light to temperature map
                    if line.strip() == "light-to-temperature map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "temp2humd"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        ligt2temp.append(entry)
                case "temp2humd":
                    # Create temperature to humidity map
                    if line.strip() == "temperature-to-humidity map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "humd2locn"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        temp2humd.append(entry)
                case "humd2locn":
                    # Create humidity to location map
                    if line.strip() == "humidity-to-location map:":
                        pass
                    elif line.strip() == "":
                        inputSection = "skip"
                    else:
                        entry: list[int] = [int(i) for i in line.split()]
                        humd2locn.append(entry)
                case _:
                    pass
        locn: int = 0
        while locn >= 0:
            humd = findDest2SourceOffset(humd2locn,locn)
            temp = findDest2SourceOffset(temp2humd, humd)
            ligt = findDest2SourceOffset(ligt2temp, temp)
            watr = findDest2SourceOffset(watr2ligt, ligt)
            fert = findDest2SourceOffset(fert2watr, watr)
            soil = findDest2SourceOffset(soil2fert, fert)
            seed = findDest2SourceOffset(seed2soil, soil)
            for i in range(0, len(seedsEntry), 2):
                if (seed >= seedsEntry[i] and seed <= (seedsEntry[i] + seedsEntry[i+1])):
                    print (f"Minimum location is {locn}")
                    exit()
            locn += 1

if __name__ == "__main__":
    #part1()
    #part2()
    part2Improved()