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
        minHeap = []

        answer = []

        heapq.heapify(minHeap)


        for key in dic :
            
            v = dic.get(key)
            if (v != None) :
                heapq.heappush(minHeap, (v,key))

            if (len(minHeap) > k) :
                heapq.heappop(minHeap)

        for item in minHeap :
            answer.append(item[1])
            

        

        

        return answer
        