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
  gameNo = int(line[0][pointer + 1:])
  line = line[1].split('|')
  winners = line[0].split(' ')
  winners = [int(i) for i in winners if i]
  numbers = line[1].split(' ')
  numbers = [int(i) for i in numbers if i]
  return gameNo, numbers, winners

class Card:

  def __init__(self, id, numbers, winners):
    self.id = id
    self.numbers = numbers
    self.winners = winners
    self.copies = 1
    self.count = 0
    self.score = 0
    
  def countCard(self):
    for number in self.numbers:
      if number in self.winners:
        self.count += 1
        
  def addCopies(self,number):
    self.copies += number

  def scoreCard(self):
    if self.count>0:
      self.score = 1 * (2**(self.count -1))

def processCard(card, cardList):
  card.countCard()
  card.scoreCard()
  for i in range(card.id, card.id + card.count):
    cardList[i].addCopies(card.copies)

def buildCardList(data):
  cardList = []
  for line in data:
    gameNo, numbers, winners = parseLine(line)
    cardList.append(Card(gameNo, numbers, winners))
  return cardList

def main():
  data = filehandling(FILEPATH)
  cardList = buildCardList(data)
  for card in cardList:
    processCard(card, cardList)
  cardCount = 0
  score = 0
  for card in cardList:
    score += card.score
    cardCount += card.copies

  print(f'Part 1: The score of the cards is {score}\nPart 2: The total number of cards is {cardCount}')
  return score, cardCount


if __name__ == "__main__":
  main()
