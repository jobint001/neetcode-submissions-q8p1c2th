class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s= len(nums)
        prefix,postfix, res = [0]*s, [0]*s, [0]*s

        for i in range(0,len(nums)):
            if i==0:
                prefix[i]=1*nums[i]
            else:

                prefix[i]=prefix[i-1]*nums[i]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                postfix[i]=1*nums[i]
            else:

                postfix[i]=postfix[i+1]*nums[i]
        print(postfix)
        for i in range(0,len(nums)):
            if i==0:
                res[i]= 1*postfix[i+1]
            elif i== len(nums)-1:
                res[i] = prefix[i-1]*1
            else:
                res[i] = prefix[i-1]*postfix[i+1]
        return res
            

