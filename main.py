FILEPATH = "calibration"

def filehandling(filename):
  with open(filename, "r") as f:
    data = f.readlines()
  return data

def findNumber(inputString):
  for c in inputString:
    if c.isdigit():
      return c
  return None

def findNumberPair(inputString):
  numberPair = ""
  numberPair += findNumber(inputString)
  reversedString = inputString[::-1]
  numberPair += findNumber(reversedString)
  return int(numberPair)

if __name__ == "__main__":
  data = filehandling(FILEPATH)
  total = 0
  for line in data:
    line = line.strip()
    findNumberPair(line)
    total += findNumberPair(line)
  print(total)
