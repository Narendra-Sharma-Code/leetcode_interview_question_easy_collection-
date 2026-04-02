nums = [1,2,3,4,5,6,7], k = 3

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reversed(start,end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -=1
        reversed(0,n-1)
        reversed(0,k-1)
        reversed(k,n-1)
    