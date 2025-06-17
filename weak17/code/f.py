class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return self.sub(nums,k) - self.sub(nums,k-1)
    def sub(self, nums, k):
        left = 0
        di = {}
        valid = 0 
        for right in range(len(nums)):
            di[nums[right]] = di.get(nums[right],0) + 1 
            while len(di) > k :
                if di[nums[left]] == 1 :
                    del di[nums[left]]
                else :
                    di[nums[left]] -= 1
                left += 1
            if len(di) <= k :
                valid += (right - left + 1)
        return valid
                
                
    
s = Solution()
print(s.subarraysWithKDistinct([1,2,1,3,4],3))

