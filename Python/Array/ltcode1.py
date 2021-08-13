# Find problem statement here: https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589/
# The code here is pretty shit, so many nested for loops. I will update the code after some research of the given solutions.

class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        if len(pieces) == 1 and len(arr) > 1:
            if arr == pieces[0]:
                return True
            return False
        tempArr = []
        newArr = []
        for number in arr:
            for i in pieces:
                for j in i:
                    if j == number:
                        if i in tempArr:
                            continue
                        else:
                            tempArr.append(i)
        for array in tempArr:
            for number in array:
                newArr.append(number)
        print("Given array: ", arr)
        print("Array after forming pieces:", newArr)
        if newArr == arr:
            return True
        return False 

# Everything above is the solution, below is the driver code:

if __name__ == '__main__':
  arr = [5,6,7,8]
  pieces = [[6,7],[5,8]]
  solutionObj = Solution()
  print(solutionObj.canFormArray(arr, pieces))