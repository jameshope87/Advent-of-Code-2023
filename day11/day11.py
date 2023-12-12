import os
import pathlib

def filehandling(filename):
  galaxy = []
  numGalaxies = 0
  with open(filename, "r") as f:
    for line in f . readlines():
      row = []
      for c in line.strip():
        if c == '#':
          row.append(numGalaxies)
          numGalaxies += 1
        else:
          row.append(c)
      galaxy.append(row)

  return galaxy, numGalaxies

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day11input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day11test')

def getEmptyRows(galaxy: list[list[str]]) -> list[int]:
  emptyRows = []
  for ix, row in enumerate(galaxy):
    if all([c == '.' for c in row]):
      emptyRows.append(ix)
  return emptyRows

def getEmptyCols(galaxy: list[list[str]]) -> list[int]:
  emptyCols = []
  for iy in range(len(galaxy[0])):
    if all([galaxy[ix][iy] == '.' for ix in range(len(galaxy))]):
      emptyCols.append(iy)
  return emptyCols

def getGalPos(galaxy: list[list[str]]) -> dict[int,tuple[int,int]]:
  return {
    galaxy[ix][iy]: (ix,iy)
    for ix in range(len(galaxy))
    for iy in range(len(galaxy[0]))
    if galaxy[ix][iy] != '.'}

def taxiDist(point1: tuple[int,int], point2: tuple[int,int]) -> int:
  return sum([abs(point1[0] - point2[0]),abs(point1[1] - point2[1])])

def addExtra(point1: tuple[int,int], 
             point2: tuple[int,int],
             emptyRows: list[int],
             emptyCols: list[int],
             expansionFactor: int) -> int:
  extra = 0
  minx, maxx = (point1[0],point2[0]) if point1[0] < point2[0] else (point2[0],point1[0])
  for row in emptyRows:
    if minx < row < maxx:
      extra += expansionFactor - 1
  miny, maxy = (point1[1],point2[1]) if point1[1] < point2[1] else (point2[1],point1[1])
  for col in emptyCols:
    if miny < col < maxy:
      extra += expansionFactor - 1
  return extra

def main(expansionFactor = 1):
  galaxy, numGalaxies = filehandling(FILEPATH)
  galaxyPositions = getGalPos(galaxy)
  pairs = [(i,j) for i in range(numGalaxies) for j in range(i, numGalaxies) if i < j]
  emptyRows = getEmptyRows(galaxy)
  emptyCols = getEmptyCols(galaxy)
  total = sum([
      (taxiDist(galaxyPositions[i], galaxyPositions[j]) + addExtra(galaxyPositions[i], galaxyPositions[j], emptyRows, emptyCols, expansionFactor))
      for i, j in pairs
    ])
  print(f'Total distance: {total}')
  

if __name__ == "__main__":
  main(1_000_000)
