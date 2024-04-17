def calcDist(aHoldDuration: int, aRaceDuration: int) -> int:
    return (aHoldDuration * (aRaceDuration - aHoldDuration))

def isLonger(aDist: int, aDist2Beat: int) -> bool:
    return aDist > aDist2Beat

def part1() -> None:
    raceTimes: list[int] = []
    raceDistances: list[int] = []
    with open ('input.txt') as file:
        lines: list[list[str]] = file.readlines()
        # Process time line
        raceTimes = [int(i) for i in lines[0].split()[1:]]
        raceDistances = [int(i) for i in lines[1].split()[1:]]

    allPossibilities: list[int] = []
    for race in range(len(raceTimes)):
        racePossibilities = 0
        for time in range(raceTimes[race] + 1):
            if isLonger(calcDist(time, raceTimes[race]),raceDistances[race]):
                racePossibilities += 1
        allPossibilities.append(racePossibilities)
    
    answer = 0
    for possibility in allPossibilities:
        if answer == 0:
            answer += possibility
        else:
            answer *= possibility
    
    print(f'The answer to part 1 is {answer}')


def main() -> None:
    part1()

if __name__ == "__main__":
    main()