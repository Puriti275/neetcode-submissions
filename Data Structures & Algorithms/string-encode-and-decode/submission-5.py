class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Input: List[str]
        Output: str

        What we have to do: take each string in the list and put it into a string
        
        Methodology: concatenate each item into a string, separated by a character.
        IN this case, the character is a hashtag. 

        Edgecases:
        1. empty list
        2. duplicates
        3. Single entry list
        4. hashtag only list
        """

        """
        result = ""

        if(len(strs)) == 0:
            return ""

        for s in strs:
            result += str(len(s)) + "#" + s 
        
        print(result)
        return result
        """

        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        """
        Input: str
        Output: List[str]

        Methodology: Find all occurences of " ". Find the next occurence of " ",
        then add the substring between the " "'s

        Edgecases:
        1. empty string
        2. duplicates
        3. string with length 1
        4. string with just "#"

        """

        """
        result = []
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']

        if s == "":
            return [""]
        
        for char in s:
            if s[char] != '#' and s[char].lower() not in letters:
                size = s[char]
            elif s[char] == '#':
                result.append(s[char:char + 5])
            elif s[char].lower() in letters:
                

        if s == "":
            print("s == "")
            return [""]
        elif len(s) == 1:
            print("len(s) == 1")
            return [s]
        elif len(s) == 1 and s == "#":
            print("len(s) == 1 and s == #")
            return ["#"]

        s.replace(" ", "")

        return s.split('#')

        print(s)

        result = []
        space_indexes = []
        index1, index2 = 0, 0

        count = s.count("#")

        for i in range(len(s)):
            if s[i] == "#":
                space_indexes.append(i)

        print(space_indexes)

        for i in range(count):
            index1 = space_indexes[i - 1]
            index2 = space_indexes[i]
            string = s[index1 + 1:index2]

            print(string)
            result.append(string)

        return result
        """

        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
