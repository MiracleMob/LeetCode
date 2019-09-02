class Solution(object):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        if row == 0:
            return False
        col = len(board[0])
        masked = [[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if self.search_words(board, word, 0, i, j, masked, row, col):
                    return True

        return False

    def search_words(self, board, word, index, s_x, s_y, masked, row, col):
        if index == len(word) - 1:
            return board[s_x][s_y] == word[index]
        if board[s_x][s_y] == word[index]:
            masked[s_x][s_y] = True
            for direction in self.directions:
                new_x = s_x + direction[0]
                new_y = s_y + direction[1]
                if 0 <= new_x < row and 0 <= new_y < col and not masked[new_x][
                    new_y] and \
                        self.search_words(board, word, index + 1, new_x, new_y,
                                          masked, row, col):
                    return True

            masked[s_x][s_y] = False

        return False




