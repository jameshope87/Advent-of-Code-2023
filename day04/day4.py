from helpers import filehandling

FILEPATH = 'day04/day4input'
TESTPATH = 'day04/day4test'

def parseLine(line):
  line = line.split(':')
  
  pointer = len(line[0]) - 1
  character = line[0][pointer]
  while character.isdigit():
    pointer -= 1
    character = line[0][pointer]
  gameNo = int(line[0][pointer+1:])
  line = line[1].split('|')
  winners = line[0].split(' ')
  winners = [int(i) for i in winners if i]
  numbers = line[1].split(' ')
  numbers = [int(i) for i in numbers if i]
  card = [gameNo, numbers, winners]
  return card
  

def scoreCard(numbers, winners):
  count = 0
  for number in numbers:
    if  number in winners:
      count += 1
  if count > 0:
    return 1*(2**(count-1))
  else:
    return 0

def countCard(numbers, winners):
  count = 0
  for number in numbers:
    if  number in winners:
      count += 1
  return count

def part1():
  data = filehandling(FILEPATH)
  cards = []
  for line in data:
    cards.append(parseLine(line))
  total = 0
  for card in cards:
    total += scoreCard(card[1], card[2])
  return total

def addCardToQueue(card, cardStack):
  game = card[0]
  pointer = 0
  while game > cardStack[pointer][0]:
    pointer += 1
  cardStack.insert(pointer, card)

def processCard(card, cardStack, cardList):
  numbers = card[1]
  winners = card[2]
  cardNo = card[0]
  count = countCard(numbers,winners)
  for i in range(cardNo, cardNo + count):
    addCardToQueue(cardList[i], cardStack)
  return 1
  

def part2():
  data = filehandling(TESTPATH)
  cardStack = []
  cardList = []
  score = 0
  for line in data:
    cardStack.append(parseLine(line))
    cardList.append(parseLine(line))
  while len(cardStack) > 0:
    card = cardStack.pop(0)
    score += processCard(card, cardStack, cardList)
    print(score)
  return score
  
  


if __name__ == "__main__":
  pass
  #print()
  #print(part2())