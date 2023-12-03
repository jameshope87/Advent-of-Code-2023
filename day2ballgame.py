from helpers import filehandling

FILEPATH = "day2input"
MAXRED = 12
MAXGREEN = 13
MAXBLUE = 14

def parseline(line):
  gamelist = []
  parsed = line.split(":")
  parsed = parsed[1].split(";")
  for hand in parsed:
    hand = hand.split(",")
    #print(hand)
    rgblist = ['0','0','0']
    for v in hand:
      if 'red' in v:
        for c in v:
          if c.isdigit():
            rgblist[0] += c
      if 'green' in v:
        for c in v:
          if c.isdigit():
            rgblist[1] += c
      if 'blue' in v:
        for c in v:
          if c.isdigit():
            rgblist[2] += c
    for i,d in enumerate(rgblist):
      rgblist[i] = int(d)
    gamelist.append(rgblist)
  return(gamelist)
    
def parseData(data, parsedData):
  for line in data:
    parsedData.append(parseline(line))

def possChecker(game):
  for hand in game:
    if hand[0] > MAXRED or hand[1] > MAXGREEN or hand[2] > MAXBLUE:
      return False
  return True

def findFewest(game):
  fewest = [0,0,0]
  for hand in game:
    for i in range(0,3):
      if hand[i] > fewest[i]:
        fewest[i] = hand[i]
  return fewest

def findPower(fewestList):
  total = 1
  for i in fewestList:
    total *= i
  return total

def part1():
  data = filehandling(FILEPATH)
  #print(data)
  parsedData = []
  #parseline("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
  parseData(data, parsedData)
  validGames = [i+1 for i,g in enumerate(parsedData) if possChecker(g)]
  print(validGames)
  total = sum(validGames)
  print(total)

def part2():
  data = filehandling(FILEPATH)
  #print(data)
  parsedData = []
  #parseline("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
  parseData(data, parsedData)
  powerList = [findPower(findFewest(game)) for game in parsedData]
  print(sum(powerList))
  
if __name__ == "__main__":
  part2()