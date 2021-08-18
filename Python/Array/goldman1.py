# problem can be found here: https://prepinsta.com/goldman-sachs/technical-test/coding-questions/

class Taxi:
  def __init__(self, matrix):
    self.matrix = matrix
  
  def pathToStation(self):
    # we can only move right or down when going to the railway station:
    passengerCount = 0
    for row in self.matrix:
      for cell in row:
        # if passenger is detected, increment passenger count
        if cell == 1:
          passengerCount += 1
          cell = 0
        # blockade detected, then continue
        if cell == -1:
          continue
    return passengerCount
  
  def pathToAirport(self, n, m):
    # can only move upwards or left when going to the airport:
    passengerCount = 0
    for row in range(n-1, -1):
      for cell in range(m-1, -1):
        if cell == 1:
          passengerCount += 1
          cell = 0
        if cell == -1:
          continue
    return passengerCount
  
  def totalPassengers(self, n, m):
    return self.pathToAirport(n, m) + self.pathToStation()

# driver code, input is copied directly from problem:
if __name__ == '__main__':
  # test case 1:
  n = 3
  m = 3
  matrix = [
    [0,1,-1],
    [1,0,-1],
    [1,1,1]
  ]
  taxi = Taxi(matrix)
  for row in matrix:
    print(row)
  print(taxi.totalPassengers(n,m))
  # test case 2:
  n = 4
  m = 4
  matrix = [
    [0,0,0,1],
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
  ]
  taxi = Taxi(matrix)
  for row in matrix:
    print(row)
  print(taxi.totalPassengers(n,m))
  # test case 3:
  n = 2
  m = 2
  matrix = [
    [0,1],
    [-1,0]
  ]
  taxi = Taxi(matrix)
  for row in matrix:
    print(row)
  print(taxi.totalPassengers(n,m))