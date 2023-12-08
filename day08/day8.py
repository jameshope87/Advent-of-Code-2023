import os
import pathlib

def filehandling(filename):
  with open(filename, "r") as f:
    data = f.read().splitlines()
  return data

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day8input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day8test')
DIRECTIONS = ['L','R']
START = 'AAA'
END = 'ZZZ'

def parseData(data):
  directions = data.pop(0)
  maps = {}
  data.pop(0)
  for line in data:
    id = line[:3]
    left = line[7:10]
    right = line[12:15]
    maps[id] = [left,right]
  return directions, maps

def makeMove(maps, location, direction):
  return maps[location][DIRECTIONS.index(direction)]

def traverseMaze(maps, directions):
  current = START
  steps = 0
  loopLength = len(directions)
  while True:
    direction = directions[steps % loopLength]
    next = makeMove(maps,current,direction)
    steps += 1
    print(f'After {steps} step we moved {direction} from {current} to {next}')
    current = next
    if current == END:
      return steps
    #print(makeMove(maps, 'AAA', 'R'))

def traverseGhostMaze(maps, directions):
  currents = [key for key in maps.keys() if key[2] == 'A']
  steps = 0
  loopLength = len(directions)
  while True:
    direction = directions[steps%loopLength]
    nexts = [makeMove(maps,location,direction) for location in currents]
    steps += 1
    print(nexts, ' ', steps)
    currents = nexts
    if all(final[2] == 'Z' for final in currents):
      return steps


def main(part=1):
  data = filehandling(FILEPATH)
  directions, maps = parseData(data)
  #totalSteps = traverseMaze(maps, directions)
  #print(totalSteps)
  totalSteps = traverseGhostMaze(maps, directions)
  print(totalSteps)

if __name__ == "__main__":
  main()
