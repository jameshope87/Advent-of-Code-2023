import os
import pathlib
from turtle import end_fill

def filehandling(filename):
  with open(filename, "r") as f:
    data = f.read().splitlines()
  return data

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day10input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day10test')

class Loop:
  def __init__(self, loop):
    self.loop = loop
    self.start = [0,0]
    self.nextpointer = [0,0]
    self.nextpipe = ''
    self.currentpos = self.start
    self.currentpipe = ''
    self.loopLength = 0
    self.visited = []

  def findStart(self):
    for r,row in enumerate(self.loop):
      if 'S' in row:
        self.start = [r, row.index('S')]
        self.visited.append(self.start)
      
  def findFirstMove(self):
    if self.loop[self.start[0]-1][self.start[1]] in ['|','7','F']:
      self.currentpos = [self.start[0]-1, self.start[1]]
      self.currentpipe = self.loop[self.start[0]-1][self.start[1]]
    elif self.loop[self.start[0]+1][self.start[1]] in ['|','L','J']:
      self.currentpos = [self.start[0]+1, self.start[1]]
      self.currentpipe = self.loop[self.start[0]+1][self.start[1]]
    elif self.loop[self.start[0]][self.start[1]-1] in ['-','L','F']:
      self.currentpos = [self.start[0], self.start[1]-1]
      self.currentpipe = self.loop[self.start[0]][self.start[1]-1]
    elif self.loop[self.start[0]][self.start[1]+1] in ['-','J','7']:
      self.currentpos = [self.start[0], self.start[1]+1]
      self.currentpipe = self.loop[self.start[0]][self.start[1]+1]
    self.loopLength += 1
  
  def findNextMove(self):
    if self.currentpipe == '|':
      if [self.currentpos[0]-1,self.currentpos[1]] not in self.visited:
        self.nextpointer = [self.currentpos[0]-1,self.currentpos[1]]
      elif [self.currentpos[0]+1,self.currentpos[1]] not in self.visited:
        self.nextpointer = [self.currentpos[0]+1,self.currentpos[1]]
    elif self.currentpipe == '-':
      if [self.currentpos[0],self.currentpos[1]+1] not in self.visited:
        self.nextpointer = [self.currentpos[0],self.currentpos[1]+1]
      elif [self.currentpos[0],self.currentpos[1]+1] not in self.visited:
        self.nextpointer = [self.currentpos[0],self.currentpos[1]-1]
    elif self.currentpipe == 'L':
      if [self.currentpos[0],self.currentpos[1]+1] not in self.visited:
        self.nextpointer = [self.currentpos[0],self.currentpos[1]+1]
      elif [self.currentpos[0]-1,self.currentpos[1]] not in self.visited:
        self.nextpointer = [self.currentpos[0]-1,self.currentpos[1]]
    elif self.currentpipe == 'J':
      if [self.currentpos[0],self.currentpos[1]-1] not in self.visited:
        self.nextpointer = [self.currentpos[0],self.currentpos[1]-1]
      elif [self.currentpos[0]-1,self.currentpos[1]] not in self.visited:
        self.nextpointer = [self.currentpos[0]-1,self.currentpos[1]]
    elif self.currentpipe == '7':
      if [self.currentpos[0]+1,self.currentpos[1]] not in self.visited:
        self.nextpointer = [self.currentpos[0]+1,self.currentpos[1]]
      elif [self.currentpos[0],self.currentpos[1]-1] not in self.visited:
        self.nextpointer = [self.currentpos[0],self.currentpos[1]-1]
    elif self.currentpipe == 'F':
      if [self.currentpos[0],self.currentpos[1]+1] not in self.visited:
        self.nextpointer = [self.currentpos[0],self.currentpos[1]+1]
      elif [self.currentpos[0]+1,self.currentpos[1]] not in self.visited:
        self.nextpointer = [self.currentpos[0]+1,self.currentpos[1]]
    self.nextpipe = self.loop[self.nextpointer[0]][self.nextpointer[1]]
    self.visited.append(self.currentpos)
    self.currentpos = self.nextpointer
    self.currentpipe = self.nextpipe
    self.loopLength += 1

def parseData(data):
  loop = []
  for row in data:
    loop.append(row)
  return loop

def main(part=1):
  data = filehandling(TESTPATH)
  mainMap = Loop(parseData(data))
  print(mainMap.start)
  mainMap.findFirstMove()
  while mainMap.nextpipe != 'S':
    mainMap.findNextMove()
    print(mainMap.loopLength)

  

if __name__ == "__main__":
  main()
