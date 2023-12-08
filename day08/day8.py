import os
import pathlib
import math

def filehandling(filename):
  with open(filename, "r") as f:
    data = f.read().splitlines()
  return data

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day8input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day8test')
TESTPATH2 = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day8test2')
DIRECTIONS = ['L','R']
START = 'AAA'
END = 'ZZZ'
directions = ''
maps = {}

def parseData(data):
  global directions
  directions = data.pop(0)
  data.pop(0)
  for line in data:
    id = line[:3]
    left = line[7:10]
    right = line[12:15]
    maps[id] = [left,right]

def traverseMaze(start, end, part2 = False):
  steps = 0
  loopLength = len(directions)
  while True:
    direction = directions[steps % loopLength]
    start = maps[start][DIRECTIONS.index(direction)]
    steps += 1
    if start == end or (part2 and start[-1] == end[-1]):
      return steps

def main(part=1):
  data = filehandling(FILEPATH)
  parseData(data)
  totalSteps = traverseMaze(START, END)
  print(totalSteps)
  #part 2
  #data = filehandling(TESTPATH2)
  #parseData(data)
  starts = [key for key in maps.keys() if key[2] == 'A']
  totalSteps = math.lcm(*[traverseMaze(start, END, True) for start in starts])
  print(totalSteps)

if __name__ == "__main__":
  main()
