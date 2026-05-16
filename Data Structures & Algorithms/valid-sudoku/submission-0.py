class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Input: List[List[str]]
        Output: bool

        matching: for loops, hashmaps, lists, stacks

        Time & Space Complexity: O(n^2)
        """

        """
        result = True
        duplicates = set()
        column = []
        square = []

        print("Passing through rows")

        # one pass to check rows
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    duplicates.add(board[i][j])
            
            filtered = [x for x in board[i] if x != '.']

            if(len(duplicates) != len(filtered)):
                return False    
            
            print(duplicates)
            duplicates.clear()
        
        print("Passing through columns")

        # second pass to check cols
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    duplicates.add(board[j][i])
                    column.append(board[j][i])
                    print(duplicates)

            filtered = [x for x in column if x != '.']

            if len(duplicates) != len(column):
                return False 
            
            print(duplicates)
            duplicates.clear()
            column.clear()

        print("Passing through squares")

        # third pass to check 3 x 3
        for i in range(len(board), 3):
            for j in range(3, len(board[i]), 3):
                print(f"i: {i}, j: {j}")

                square.append(board[0 + i][i:j - 1])
                square.append(board[1 + i][i:j - 1])
                square.append(board[2 + i][i:j - 1])
                print(square)

            filtered = [x for x in square if x != '.']

            for j in range(len(filtered)):
                duplicates.add(filtered[j])

            print(f"filtered: {filtered}")

            if len(duplicates) != len(filtered):
                return False

            print(duplicates)
            square.clear()
            duplicates.clear()

        return True
        """

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True