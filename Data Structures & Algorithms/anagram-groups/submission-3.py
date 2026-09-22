from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 알파벳 다 존재하는지 확인 (a 몇개인지 b 몇개인지)

        # a~z 26개 에다가 (00000100) 이런식으로 각 알파벳 갯수 체크 -> 일치하는거 있으면 같이 넣기

        # 26자리수 : cat, hat 

        # 이런식으로 저장하고 마지막에 해시테이블 순회해서 각 키값 묶어서 return 

        dic = defaultdict(list)

        
        
        for s in strs :

            alpas = [0] * 26
            
            for c in s :
                alpas[ord(c) - 97] += 1

            k = '-'.join(map(str, alpas))

            dic[k].append(s)

        answer = []

        for k in dic :

            answer.append(dic[k])

        return answer
            
 




        
        
        