FILEPATH = "calibration"
NUMBER_LIST = ["one","two","three","four","five","six","seven","eight","nine"]

def filehandling(filename):
  with open(filename, "r") as f:
    data = f.readlines()
  return data

def findNumber(inputString,reversed):
  position2 = 100
  position1 = 100
  for c in inputString:
    if c.isdigit():
      number1 = c
      position1 = inputString.find(c)
      break
  for n in NUMBER_LIST:
    if reversed:
      n = n[::-1]
    position2temp = inputString.find(n)
    if position2temp < position2 and position2temp > -1:
      position2 = position2temp
      number2 = n
  if position1 < position2:
    return number1
  else:
    if reversed:
      return str(NUMBER_LIST.index(number2[::-1])+1)
    return str(NUMBER_LIST.index(number2)+1)

def findNumberPair(inputString):
  numberPair = ""
  numberPair += findNumber(inputString, False)
  reversedString = inputString[::-1]
  numberPair += findNumber(reversedString, True)
  return int(numberPair)

if __name__ == "__main__":
#  print(findNumberPair("fivecqkzbllhshphlseven4ftfivevl3"))
  data = filehandling(FILEPATH)
  total = 0
  for line in data:
    line = line.strip()
    findNumberPair(line)
    total += findNumberPair(line)
  print(total)