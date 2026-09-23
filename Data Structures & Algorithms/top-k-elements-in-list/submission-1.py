from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # k = 2 -> 첫번째 frequent , 2번째 frequent 

        """
        ex 1 )

        1 : 1

        2 : 2 

        3 : 3 

        2,3


        """

        dic = defaultdict(int)

        for num in nums :
            
            dic[num] += 1

        sor = sorted(dic.items(), key = lambda x: -x[1])


        # print(sor)
        answer = []

        for idx in range(k) :
            
            k, v = sor[idx]

            answer.append(k)

        return answer
        