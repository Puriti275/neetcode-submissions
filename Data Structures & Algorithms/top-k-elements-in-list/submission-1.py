class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Input: List[int]
        Output: List[int]

        Methodology: iterate through the list and add frequencies to a
        hashmap. The key is the number, and the value is the frequency

        You're going to return the k most frequent elements. To do this,
        we can sort the hashmap by the greatest values, and add them to
        the result list. Afterward, we return it.

        edge cases:
        1. empty array
        2. 
        """

        result = []
        hash = defaultdict(int)

        for num in nums:
            hash[num] += 1

        print(hash)

        sorted_hash = dict(sorted(hash.items(), key=lambda item: item[1], reverse=True))

        sorted1 = list(sorted_hash)

        print(sorted1)

        for i in range(k):
            result.append(sorted1[i])

        return result