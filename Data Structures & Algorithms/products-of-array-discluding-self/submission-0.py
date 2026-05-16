class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: List[int]
        Output: List[int]

        Methodology: Pre and Post. O(n), two passes of list

        """

        result = []
        pre = 1
        post = 1

        for i in range(len(nums)):
            result.append(pre)
            pre *= nums[i]

        print(result)

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]
        
        return result