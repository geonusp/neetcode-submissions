class Solution:
    def twoSum(self, nums: List[int], target: int):

        ans = []

        dic = {}
        
        for i in range(len(nums)) :
            # 보완되는게 있는지 확인 
            comple = target - nums[i]

            if (comple in dic) :
                return [dic[comple], i]

            # 없으면 딕셔너리 
            dic[nums[i]] = i


        return ans  

        