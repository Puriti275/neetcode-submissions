class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        characters1, characters2 = {}, {}

        for i in range(len(s)):
            characters1[s[i]] = 1 + characters1.get(s[i], 0)
            characters2[t[i]] = 1 + characters2.get(t[i], 0)

        print(characters1)
        print(characters2)

        return characters1 == characters2
                    
