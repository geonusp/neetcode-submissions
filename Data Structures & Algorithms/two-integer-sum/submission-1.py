class Solution:
    def twoSum(self, nums: List[int], target: int):

        
        answer = []

        isBreak = False

        for i in range(len(nums)) :

            if (isBreak) :
                break

            for j in range(len(nums)) :
                if (i == j) :
                    continue

                res = nums[i] + nums[j]
                if (res == target) :
                  answer.append(i)
                  answer.append(j)  
                  isBreak = True
                  break

        answer.sort()

        return answer

        