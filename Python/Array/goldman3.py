# Problem can be found here: https://prepinsta.com/goldman-sachs/technical-test/coding-questions/

def max(a, b):
  if a > b:
    return a
  return b

def min(a, b):
  if a < b:
    return a
  return b

def fountain(arr, size):
  lowerLimit = 0
  upperLimit = 0
  count = 0
  temp = 0
  if len(arr) == 0:
    return -1
  
  for i in range (0,size):
    lowerLimit = max(((i+1) - arr[i]), 1)
    upperLimit = min(((i+1) + arr[i]), size)
    if lowerLimit == 1 and upperLimit == size:
      return 1
    if lowerLimit == 1 and upperLimit < size:
      temp = upperLimit
      count += 1
    elif lowerLimit == temp+1 and upperLimit <= size:
      temp = upperLimit
      count += 1
  return count

# driver code:

if __name__ == '__main__':
  arr = [0, 1, 2, 5, 9]
  print ("The location array is: ", arr)
  print ("Fountains to be activated: ", fountain(arr, len(arr)))
  arr = [1,1,1]
  print ("The location array is: ", arr)
  print ("Fountains to be activated: ", fountain(arr, len(arr)))