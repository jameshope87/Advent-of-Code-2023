from day06.day6 import main
import time

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