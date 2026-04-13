class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod=1
        count=0
        zeroIndex=-1
        countZero=0
        for n in nums:
            if n == 0 and countZero ==0:
                zeroIndex = count
                countZero+=1
                continue
            count +=1
            prod*=n
        
        res = []
        for i in range(0,len(nums)):
            if zeroIndex == -1:

                res.append(int(prod/nums[i]))
            elif i == zeroIndex:
                res.append(prod)
            else :
                res.append(0)

        return res