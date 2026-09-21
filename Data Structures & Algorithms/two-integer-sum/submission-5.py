class Solution:
    def twoSum(self, nums: List[int], target: int):

        ans = []

        dic = {}
        
        for i in range(len(nums)) :
            dic[nums[i]] = i

        for i in range(len(nums)) :
            if (target - nums[i] in dic) :
                j = dic.get(target-nums[i]) 
                if (i == j) :
                    continue
                ans.append(i)
                ans.append(j)
                break
        


        ans.sort()

        return ans  

        