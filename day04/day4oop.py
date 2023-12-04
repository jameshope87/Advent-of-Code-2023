from day04.day4 import countCard
from helpers import filehandling

FILEPATH = 'day04/day4input'
TESTPATH = 'day04/day4test'


class Card:

  def __init__(self, id, numbers, winners):
    self.id = id
    self.numbers = numbers
    self.winners = winners
    self.copies = 1
    self.count = 0
    for number in self.numbers:
      if number in self.winners:
        self.count += 1

  def countCard(self):
    for number in self.numbers:
      if number in self.winners:
        self.count += 1
  def addCopies(self,number):
    self.copies += number

def parseLine(line):
  line = line.split(':')
  pointer = len(line[0]) - 1
  character = line[0][pointer]
  while character.isdigit():
    pointer -= 1
    character = line[0][pointer]
  gameNo = int(line[0][pointer + 1:])
  line = line[1].split('|')
  winners = line[0].split(' ')
  winners = [int(i) for i in winners if i]
  numbers = line[1].split(' ')
  numbers = [int(i) for i in numbers if i]
  return gameNo, numbers, winners

def scoreCard(numbers, winners):
  count = 0
  for number in numbers:
    if number in winners:
      count += 1
  if count > 0:
    return 1 * (2**(count - 1))
  else:
    return 0

def part1():
  data = filehandling(FILEPATH)
  cards = []
  for line in data:
    cards.append(parseLine(line))
  total = 0
  for card in cards:
    total += scoreCard(card[1], card[2])
  return total

def processCard(card, cardList):
  for i in range(card.id, card.id + card.count):
    cardList[i].addCopies(card.copies)

def part2():
  data = filehandling(FILEPATH)
  cardList = []
  score = 0
  for line in data:
    gameNo, numbers, winners = parseLine(line)
    cardList.append(Card(gameNo, numbers, winners))
  for card in cardList:
    processCard(card, cardList)
  for card in cardList:
    score += card.copies
  return score


if __name__ == "__main__":
  pass
