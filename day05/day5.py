from helpers import filehandling

FILEPATH = 'day05/day5input'
TESTPATH = 'day05/day5test'

def parseData(data):
  seeds = data.pop(0)
  seeds = seeds.split(':')[1]
  seeds = seeds.split(' ')
  seedList = [Seed(int(i)) for i in seeds if i]
  mapList = []
  data.pop(0)
  dest = []
  source = []
  length = []
  while len(data) >0:
    line = data.pop(0)
    if line == '':
      mapList.append(Map(id,source, dest))
    elif line[0] in 'abcdefghijklmnopqrstuvwzyx':
      id = line
      dest = []
      source = []
      length = []
    elif line[0].isdigit():
      line = line.split(' ')
      destStart = int(line[0])
      sourceStart = int(line[1])
      length = int(line[2])
      destEnd = destStart + length
      sourceEnd = sourceStart + length
      dest.append([destStart,destEnd])
      source.append([sourceStart, sourceEnd])
  mapList.append(Map(id,source, dest))
  return seedList, mapList

class Map:
  def __init__(self, id, source, dest):
    self.id = id
    self.source = source
    self.dest = dest

class Seed:

  def __init__(self, id):
    self.id = id
    self.soil = id
    self.fertilizer = id
    self.water = id
    self.light = id
    self.temperature = id
    self.humidity = id
    self.location = id
    
  def mapvalue(self, input, source, destination):
    output = input
    for i in range(len(source)):
      if input > source[i][0] and input < source[i][1]:
        diff = input - source[i][0]
        output = destination[i][0] + diff
    return output

def main():
  data = filehandling(FILEPATH)
  seedList, mapList = parseData(data)
  minLocation = None
  for seed in seedList:
    for i in range(len(mapList)):
      map = mapList[i]
      match i:
        case 0:
          seed.soil = seed.mapvalue(seed.id,map.source, map.dest)
        case 1:
          seed.fertilizer = seed.mapvalue(seed.soil,map.source, map.dest)
        case 2:
          seed.water = seed.mapvalue(seed.fertilizer,map.source, map.dest)
        case 3:
          seed.light = seed.mapvalue(seed.water,map.source, map.dest)
        case 4:
          seed.temperature = seed.mapvalue(seed.light,map.source, map.dest)
        case 5:
          seed.humidity = seed.mapvalue(seed.temperature,map.source, map.dest)
        case 6:
          seed.location = seed.mapvalue(seed.humidity,map.source, map.dest)
    if minLocation == None or seed.location < minLocation:
      minLocation = seed.location
  print(f'The location of the first seed to be planted is {minLocation}')

if __name__ == "__main__":
  main()
