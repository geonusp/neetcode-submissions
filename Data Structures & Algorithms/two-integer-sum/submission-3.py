class Solution:
    def twoSum(self, nums: List[int], target: int):

        ans = []

        dic = {}
        
        for i in range(len(nums)) :
            dic[nums[i]] = target - nums[i]
            if (target-nums[i] in dic ) :
                
                j = nums.index(target-nums[i])
                if (i == j) :
                    continue

                ans.append(i)
                ans.append(j)

                print(ans)

                break


        ans.sort()

        return ans  

        