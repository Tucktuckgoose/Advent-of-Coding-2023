def part1():
    totalPoints = 0
    with open('input.txt') as file:
        for line in file:
            shortenedLine = line[10:] # Get rid of the card information
            winnersLong, mineLong = shortenedLine.split("|")
            winners = winnersLong.split()
            mine = mineLong.split()
            matches = 0
            for aNum in mine:
                for aWinner in winners:
                    if (aNum == aWinner):
                        matches += 1
            score = 0
            if matches > 0:
                score = 1
                for i in range (matches):
                    if i > 0:
                        score = score * 2

            totalPoints += score

    print(totalPoints)

def part2():
    totalCards = 0
    cardCopiesDict = {}
    winnersDict = {}
    mineDict = {}

    with open('input.txt') as file:
        i = 1
        for line in file:
            cardCopiesDict[i] = 1
            shortenedLine = line[10:] # Get rid of the card information
            winnersLong, mineLong = shortenedLine.split("|")
            winners = winnersLong.split()
            mine = mineLong.split()
            winnersDict[i] = winners
            mineDict[i] = mine
            i += 1
    
    for i in range(1,len(cardCopiesDict)+1):
        matches = 0
        for aNum in mineDict[i]:
            for aWinner in winnersDict[i]:
                if (aNum == aWinner):
                    #print(aNum + " matches " + aWinner)
                    matches += 1
                #else:
                    #print(aNum + " does not match " + aWinner)
        #print("Card " + str(i) + " had " + str(matches) + " matches on the card.")
        for j in range(1, matches + 1):
            #numCopies = cardCopiesDict[i + j]
            #numCopies += 1
            cardCopiesDict[i + j] += cardCopiesDict[i]
        totalCards += cardCopiesDict[i]

    print(totalCards)
    #print(cardCopiesDict)

if __name__ == "__main__":
    #part1()
    part2()