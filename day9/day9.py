import os
import pathlib
from turtle import end_fill

def filehandling(filename):
  with open(filename, "r") as f:
    data = f.read().splitlines()
  return data

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day9input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day9test')

class Sequence:
  def __init__(self, sequ):
    self.sequ = sequ
    self.differences = []
    self.findDifferences()
    self.findNextTerm()

  def findDifferences(self):
    diffs = self.sequ
    while len(diffs)>2:
      diffs = [e1 - e2 for (e1, e2) in zip(diffs[1:], diffs)]
      self.differences.append(diffs)
      if all([(x == 0) for x in diffs]):
        break
  
  def findNextTerm(self):
    for i in range(len(self.differences)-1,0,-1):
      self.differences[i-1].append(self.differences[i-1][-1]+self.differences[i][-1])
      self.differences[i-1].insert(0, self.differences[i-1][0] - self.differences[i][0])
    self.sequ.append(self.sequ[-1]+self.differences[0][-1])
    self.sequ.insert(0, self.sequ[0]-self.differences[0][0])
  


def parseData(data):
  sequences = []
  for sequence in data:
    sequence = sequence.split()
    sequences.append(Sequence([int(x) for x in sequence]))
  return sequences

def main(part=1):
  data = filehandling(FILEPATH)
  sequences = parseData(data)
  endTotal = 0
  startTotal = 0
  for sequence in sequences:
    endTotal += sequence.sequ[-1]
    startTotal += sequence.sequ[0]
  print(endTotal, startTotal)
  

if __name__ == "__main__":
  main()
