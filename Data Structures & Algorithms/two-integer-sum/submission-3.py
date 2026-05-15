class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # how to solve it?
        """  Hashmap maybe? store the numbers in the hashmap, and then
        find it's complement. For example, [3,4,5,6] with a target of 7.
        
        We can subtract 7 by the first element, and search for its difference.

        """

        hash = {}

        for i, n in enumerate(nums):
            hash[n] = i

        print(hash)
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash and hash[diff] != i:
                return [i, hash[diff]]
        return []


        