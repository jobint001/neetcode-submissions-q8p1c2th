class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums= sorted(nums)
        result= []
        for i,num in enumerate(snums):
            left=i+1
            right=len(nums)-1
            if i>0 and num == snums[i-1]:
                continue
          
            while left<right:
                if snums[i]+snums[left]+snums[right]>0:
                    right-=1
                elif snums[i]+snums[left]+snums[right]<0:
                    left+=1
                else:
                    result.append([snums[i],snums[left],snums[right]])
                    left+=1
                    while snums[left] == snums[left-1] and left<right:
                        left+=1


        return result