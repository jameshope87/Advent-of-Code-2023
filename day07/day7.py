from helpers import filehandling
from collections import Counter

FILEPATH = 'day07/day7input'
TESTPATH = 'day07/day7test'
CARDLIST = '23456789TJQKA'
TYPES = [
    'High Card', 'Pair', 'Two Pair', 'Three of a Kind', 'Full House',
    'Four of a Kind', 'Five of a Kind'
]


class Hand:

  def __init__(self, cards, bid):
    self.cards = cards
    self.cardString = [
        ''.join(cards).replace('A', 'E').replace('J', 'B').replace(
            'Q', 'C').replace('K', 'D').replace('T', 'A'),
        ''.join(cards).replace('A', 'E').replace('J', '1').replace(
            'Q', 'C').replace('K', 'D').replace('T', 'A')
    ]
    self.type = 0
    self.rank = 0
    self.bid = bid

  def wildCardRankup(self):
    if (self.type == 6 and 'J' in self.cards) or (self.type == 5
                                                  and 'J' in self.cards):
      self.type = 7
    elif (self.type == 4
          and 'J' in self.cards) or (self.type == 3
                                     and self.cards.count('J') == 2):
      self.type = 6
    elif self.type == 3 and self.cards.count('J') == 1:
      self.type = 5
    elif self.type == 2 and 'J' in self.cards:
      self.type = 4
    elif self.type == 1 and 'J' in self.cards:
      self.type = 2

  def determineHandType(self):
    counter = Counter(self.cards)
    cardCounts = counter.most_common()
    if cardCounts[0][1] == 5:
      self.type = 7
    elif cardCounts[0][1] == 4:
      self.type = 6
    elif cardCounts[0][1] == 3 and cardCounts[1][1] == 2:
      self.type = 5
    elif cardCounts[0][1] == 3:
      self.type = 4
    elif cardCounts[0][1] == 2 and cardCounts[1][1] == 2:
      self.type = 3
    elif cardCounts[0][1] == 2:
      self.type = 2
    else:
      self.type = 1
    #print(cardCounts, self.type)


def parseData(data):
  hands = []
  for line in data:
    cards = []
    for i in range(0, 5):
      cards.append(line[i])
    bid = int(line[6:])
    hands.append(Hand(cards, bid))
  return hands


def listSorter(items, part):
  for i in range(1, len(items)):
    current = items[i]
    i2 = i
    while i2 > 0 and items[i2 - 1].cardString[part - 1] > current.cardString[
        part - 1]:
      items[i2] = items[i2 - 1]
      i2 -= 1
    items[i2] = current


def main(part=1):
  data = filehandling(FILEPATH)
  hands = parseData(data)
  for hand in hands:
    hand.determineHandType()
    if part == 2:
      hand.wildCardRankup()
  highCard = [hand for hand in hands if hand.type == 1]
  listSorter(highCard, part)
  pairs = [hand for hand in hands if hand.type == 2]
  listSorter(pairs, part)
  twoPairs = [hand for hand in hands if hand.type == 3]
  listSorter(twoPairs, part)
  threeKind = [hand for hand in hands if hand.type == 4]
  listSorter(threeKind, part)
  fullHouse = [hand for hand in hands if hand.type == 5]
  listSorter(fullHouse, part)
  fourKind = [hand for hand in hands if hand.type == 6]
  listSorter(fourKind, part)
  fiveKind = [hand for hand in hands if hand.type == 7]
  listSorter(fiveKind, part)
  sortedHands = highCard + pairs + twoPairs + threeKind + fullHouse + fourKind + fiveKind
  p = 0
  for rank, hand in enumerate(sortedHands):
    wins = hand.bid * (rank + 1)
    p += wins
#    print(
#        f'Hand {"".join(hand.cards)} is a {TYPES[hand.type - 1]} has #rank {rank+1}, bid {hand.bid} and wins {wins}. The total is {p}.'
#    )
  return p


if __name__ == "__main__":
  main()
