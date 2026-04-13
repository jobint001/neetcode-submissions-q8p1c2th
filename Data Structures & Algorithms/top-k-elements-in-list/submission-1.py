class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=dict()
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1

        sorted_dic = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))
        result=list()
        i=1
        for key,value in sorted_dic.items():
            if i <=k:
                result.append(key)
                i+=1
            else:
                pass
        return result