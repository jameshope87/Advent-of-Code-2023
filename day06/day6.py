import os
import pathlib
import time

def filehandling(filename):
  with open(filename, "r") as f:
    data = f.read().splitlines()
  return data

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day6input')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day6test')

class Race:

  def __init__(self, time, distance):
    self.time = time
    self.distance = distance
    self.wins = 0
    self.minwinningtime = 0
    self.maxwinningtime = 0

  def resolveRace1(self):
    for option in range(self.time):
      #print(self.time - option)
      travelled = option * (self.time - option)
      if travelled > self.distance:
        self.wins += 1

  def resolveRace2(self):
    for option in range(self.time):
      travelled = option * (self.time - option)
      if travelled > self.distance:
        self.minwinningtime = option
        self.maxwinningtime = self.time - option
        self.wins = self.maxwinningtime - self.minwinningtime + 1
        break

  def resolveRacebin(self):
    start = 0
    end = self.time
    found = False
    while start <= end and not found:
      option = (start+end) // 2
      travelled = option * (self.time - option)
      if travelled == self.distance:
        option = option + 1
        found = True
      elif travelled < self.distance:
        start = option + 1
        option += 1
      else:
        end = option - 1
    self.minwinningtime = option
    self.maxwinningtime = self.time - (option)
    self.wins = self.maxwinningtime - self.minwinningtime + 1

def parseData(data):
  races = []
  line = data.pop(0)
  times = [x for x in line.split(':')[1].split(' ') if x]
  bigracetime = int(''.join(times))
  times = [int(x) for x in times]
  line = data.pop(0)
  distances = [x for x in line.split(':')[1].split(' ') if x]
  bigracedist = int(''.join(distances))
  distances = [int(x) for x in distances]
  for time, distance in zip(times, distances):
    races.append(Race(time, distance))
  bigrace = Race(bigracetime, bigracedist)
  return races, bigrace


def main(bin=True):
  data = filehandling(FILEPATH)
  races, bigrace = parseData(data)
  p = 1
  for race in races:
    if bin:
      race.resolveRacebin()
    else:
      race.resolveRace2()
    #print(race.wins)
    p *= race.wins
  if bin:
    bigrace.resolveRacebin()
  else:
    bigrace.resolveRace2()
  return p, bigrace.wins


if __name__ == "__main__":
  #main()
  start_time = time.time()
  part1, part2 = main(False)
  print(f"The answer to part 1 is {part1}")
  print(f"The answer to part 2 is {part2}")
  end_time = time.time()
  print(f'The program took {end_time-start_time} to execute with a linear search')
  start_time = time.time()
  part1, part2 = main(True)
  print(f"The answer to part 1 is {part1}")
  print(f"The answer to part 2 is {part2}")
  end_time = time.time()
  print(f'The program took {end_time-start_time} to execute with a binary search')