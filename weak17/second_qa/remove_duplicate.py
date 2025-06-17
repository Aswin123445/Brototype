class Solution:
    def numberOfSubarrays(self, nums: int, k: int) -> int:
        odd_count = 0 
        left = 0 
        sumi = 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0 :
                odd_count += 1 
                while (right - left + 1) >= k :
                    if odd_count == k:
                        sumi += 1 
                    elif odd_count > k:
                        if nums[left] % 2 != 0 :
                            odd_count -= 1 
                        left += 1 
                    
s = Solution()
s.numberOfSubarrays([1,1,2,1,1],3)