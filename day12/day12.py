import os
import pathlib
from functools import cache

#FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day12input')
#TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), 'day12test')

def filehandling(filename='input'):
  currDir = os.path.dirname(os.path.realpath(__file__))
  inputFile = os.path.join(currDir,filename)
  with open(inputFile, "r") as f:
    data = f.read().strip().split('\n')
  return data

@cache
def countBlock(block):
  numUnknown = block.count('?')
  numDamaged = block.count('#')
  return numDamaged, numUnknown

@cache
def getBlockPerm(block, nums):
  numDamaged, numUnknown = countBlock(block)
  totalDamaged = sum(nums)
  totalUnkown = max(len(nums) - 1, 0)
  if ((totalDamaged > numDamaged + numUnknown)
      or (totalUnkown > numUnknown)
      or (totalDamaged + totalUnkown > len(block))
      or (numDamaged > totalDamaged)):
    return 0
  if (totalDamaged == numDamaged) and '?' not in block:
    return 1
  total = 0
  for i, char in enumerate(block):
    if char == '?':
      total += getPerms(block[:i] + ' ' + block[i+1:], nums)
      total += getPerms(block[:i] + '#' + block[i+1:], nums)
      break
  return total

@cache
def getPerms(config, nums):
  config = config.split(' ',1)
  #print(config)
  if len(config) == 1:
    out = getBlockPerm(config[0], nums)
    return out
  return sum(getPerms(config[0], nums[:i]) * getPerms(config[1], nums[i:]) for i in range(len(nums)+1))

def main(filename = 'input', part2 = True):
  data = filehandling(filename)
  total = 0
  for line in data:
    #print(line)
    config, nums = line.split(' ')
    if part2:
      config = '?'.join([config]*5)
      nums = ','.join([nums]*5)
    #print(config)
    config = ' '.join(config.replace('.',' ').split())
    #print(config)
    nums = tuple(int(i) for i in nums.split(','))
    total += getPerms(config,nums)
  print(total)

  

if __name__ == "__main__":
  main('test')
