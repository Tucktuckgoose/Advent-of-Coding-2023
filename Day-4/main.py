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

if __name__ == "__main__":
    part1()
    #part2()