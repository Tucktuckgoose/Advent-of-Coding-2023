import sys

digits = ['0','1','2','3','4','5','6','7','8','9']

def part1():
    with open('input.txt') as file:
        numbers = []
        for line in file:
            first = '-99'
            last = '-99'
            for char in line:
                if char in digits:
                    first = char
                    break
            for char in line[::-1]:
                if char in digits:
                    last = char
                    break
            myNumStr = first + last
            myNumInt = int(myNumStr)
            numbers.append(myNumInt)
        sum = 0
        for num in numbers:
            sum += num
        print(sum)

spelledNumbers = ['one','two','three','four','five','six','seven','eight','nine']

spelledDict = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

# def part2():
#     with open('input.txt') as file:
#         numbers = []
#         for line in file:
#             first = '-99'
#             last = '-99'
#             # Do it the same as before, but convert text strings to digits
#             # Not working due to things like nineight should become nine, but will become eight with this method
#             fixedLine = line
#             for spelled in spelledNumbers:
#                 fixedLine = fixedLine.replace(spelled,spelledDict[spelled])
#             for char in fixedLine:
#                 if char in digits:
#                     first = char
#                     break
#             for char in fixedLine[::-1]:
#                 if char in digits:
#                     last = char
#                     break
#             myNumStr = first + last
#             myNumInt = int(myNumStr)
#             numbers.append(myNumInt)
#         sum = 0
#         for num in numbers:
#             sum += num
#         print(sum)

def part2():
    with open('input.txt') as file:
        numbers = []
        for line in file:
            first = '99'
            last = '99'
            # Do it the same as before, but convert text strings to digits
            replaceDict = {}
            for spelled in spelledNumbers:
                firstResult = line.find(spelled)
                lastResult = line.rfind(spelled)
                replaceDict[spelled] = [firstResult,lastResult]
            newLine = line
            
            while True:
                # Need to replace by largest index first so order is maintained
                # Replace last appearance first
                # Find the largest index
                max = -1
                maxString = ''
                for key in replaceDict:
                    if (replaceDict[key][1] > max):
                        maxString = key
                        max = replaceDict[key][1]
                # Add in the digit to the string
                if (max != -1):
                    newLine = newLine[:max] + spelledDict[maxString] + newLine[max:]
                    # Remove from the dict so we don't keep adding
                    if (replaceDict[maxString][0] == replaceDict[maxString][1]):
                        replaceDict[maxString][0] = -1
                    replaceDict[maxString][1] = -1
                # If there isn't one then we have inserted all digits from the last appearance
                else:
                    break

            while True:
                # Need to replace by largest index first so order is maintained
                # All lasts have been replaced, so replace the first appearance now
                # Find the largest index
                max = -1
                maxString = ''
                for key in replaceDict:
                    if (replaceDict[key][0] > max):
                        maxString = key
                        max = replaceDict[key][0]
                # Add in the digit to the string
                if (max != -1):
                    newLine = newLine[:max] + spelledDict[maxString] + newLine[max:]
                    # Remove from the dict so we don't keep adding
                    replaceDict[maxString][0] = -1
                # If there isn't one then we have inserted all digits from the last appearance
                else:
                    break
                
            for spelled in spelledNumbers:
                first, last = replaceDict[spelled]
                if (first != -1):
                    newLine = newLine[:first] + spelledDict[spelled] + newLine[first:]
                if (last != -1 and first != last):
                    newLine = newLine[:last] + spelledDict[spelled] + newLine[last:]
            for char in newLine:
                if char in digits:
                    first = char
                    break
            for char in newLine[::-1]:
                if char in digits:
                    last = char
                    break
            myNumStr = first + last
            myNumInt = int(myNumStr)
            numbers.append(myNumInt)
        sum = 0
        for num in numbers:
            sum += num
        print(sum)

if __name__ == "__main__":
    #part1()
    part2()