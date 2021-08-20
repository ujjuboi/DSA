# Problem can be found here: https://prepinsta.com/goldman-sachs/technical-test/coding-questions/

def Anirudh(jobTray):
  count  = 0
  profit = 0
  temp   = 0
  startTime = 0
  endTime   = 0
  for i in jobTray:
    if temp > jobTray[i][2]:
      temp = jobTray[i][2]
      if startTime < jobTray[i][0] < endTime:
        print ("Here")
        profit += temp
        count  += 1
        startTime = jobTray[i][0]
        endTime   = jobTray[i][1]
  return count, profit

def employees(jobTray):
  count, profit = Anirudh(jobTray)
  totalProfit = 0
  for i in jobTray:
    totalProfit += jobTray[i][2] 
  return count - len(jobTray), totalProfit - profit

# driver code:
if __name__ == '__main__':
  jobTray    = {1: [1200, 1430, 200], 2: [1230, 1330, 500]}
  print (jobTray)
  print (employees(jobTray))