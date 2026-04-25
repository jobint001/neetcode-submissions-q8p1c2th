class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        a= 0

        while l<r:
            if a< (min(heights[l],heights[r])*(r-l)):
                a=min(heights[l],heights[r])*(r-l)
            if heights[r]<heights[l]:
                print("r:"+str(r))
                r=r-1
            else:
                l=l+1
        return a
