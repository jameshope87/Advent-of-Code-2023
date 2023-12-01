from trebuchet import filehandling, findNumberPair

FILEPATH = "calibration"


if __name__ == "__main__":
#  print(findNumberPair("fivecqkzbllhshphlseven4ftfivevl3"))
  data = filehandling(FILEPATH)
  total = 0
  for line in data:
    line = line.strip()
    findNumberPair(line)
    total += findNumberPair(line)
  print(total)