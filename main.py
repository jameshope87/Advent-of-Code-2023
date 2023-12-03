from helpers import filehandling

FILEPATH = 'day3input'


def findnumber(linenum, col, data, added):
  number = '0'
  if data[linenum][col].isdigit():
    while data[linenum][col].isdigit():
      start = col
      col -= 1
    if [linenum, start] not in added:
      added.append([linenum, start])
      for d in data[linenum][start:]:
        if d.isdigit():
          number += d
        else:
          break
  return int(number)


def parseLine(linenum, subtotal, data, added):
  for col, char in enumerate(data[linenum]):
    if char not in '.0123456789':
      subtotal += findnumber(linenum, col - 1, data, added)
      subtotal += findnumber(linenum, col + 1, data, added)
      subtotal += findnumber(linenum - 1, col - 1, data, added)
      subtotal += findnumber(linenum - 1, col, data, added)
      subtotal += findnumber(linenum - 1, col + 1, data, added)
      subtotal += findnumber(linenum + 1, col - 1, data, added)
      subtotal += findnumber(linenum + 1, col + 1, data, added)
      subtotal += findnumber(linenum + 1, col, data, added)
  return subtotal


def gearFinder(linenum, data, added):
  gearnumbers = []
  subtotal = 0
  for col, char in enumerate(data[linenum]):
    if char == '*':
      gearnumbers = []
      added = []
      gearnumbers.append(findnumber(linenum, col - 1, data, added))
      gearnumbers.append(findnumber(linenum, col + 1, data, added))
      gearnumbers.append(findnumber(linenum - 1, col - 1, data, added))
      gearnumbers.append(findnumber(linenum - 1, col, data, added))
      gearnumbers.append(findnumber(linenum - 1, col + 1, data, added))
      gearnumbers.append(findnumber(linenum + 1, col - 1, data, added))
      gearnumbers.append(findnumber(linenum + 1, col + 1, data, added))
      gearnumbers.append(findnumber(linenum + 1, col, data, added))
      while 0 in gearnumbers:
        gearnumbers.pop(gearnumbers.index(0))
      if len(gearnumbers) == 2:
        subtotal += gearnumbers[0] * gearnumbers[1]
        gearnumbers = []
  return subtotal


def part1():
  total = 0
  addedNos = []
  data = filehandling(FILEPATH)
  for i in range(len(data)):
    total += parseLine(i, 0, data, addedNos)
  return total


def part2():
  total = 0
  addedNos = []
  data = filehandling(FILEPATH)
  for i in range(len(data)):
    total += gearFinder(i, data, addedNos)
  return total


if __name__ == "__main__":
  print(part1())
  print(part2())
