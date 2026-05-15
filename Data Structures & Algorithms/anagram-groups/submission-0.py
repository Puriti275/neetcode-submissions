class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Edgecase: empty array
        edgecase: 1 element 

        hashmaps --> key is the character, value is the frequency
        use this to determine anagrams

        sample: strs = ["x", "x", "y"]
        output: [["x", "x"], ["y"]]

        iterating through the list of length n
            iterating through the characters in the list of length m

        """

        result = defaultdict(list)

        for s in strs:
            frequencies = [0] * 26

            for c in s:
                frequencies[ord(c) - ord("a")] += 1
            result[tuple(frequencies)].append(s)

        return list(result.values())


