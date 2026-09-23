from _heapq import heapify
from collections import defaultdict
import heapq

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


        # v기준으로 힙 
        temp = []

        for key in dic :
            v = dic.get(key)
            if (v != None) :
                temp.append((-v,key))

        answer = []

        heapq.heapify(temp)

        for _ in range(k) :

            item = heapq.heappop(temp)
            answer.append(item[1])

        

        return answer
        