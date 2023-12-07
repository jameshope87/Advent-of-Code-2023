def filehandling(filename):
  with open(filename, "r") as f:
    data = f.read().splitlines()
  return data

def binarySearch(items, toFind):
  found = False
  first = 0
  last = len(items - 1)