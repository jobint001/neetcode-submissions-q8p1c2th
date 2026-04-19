class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        logest= 0
        for n in nums:
            length= 0
            if n-1 not in numSet:
                k=n
                while k in numSet:
                    length +=1
                    k=k+1
                if length>logest:
                    logest=length
        return logest