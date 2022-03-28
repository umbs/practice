class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        r1, r2, c1, c2 = row1, row2, col1, col2
        while r1 <= r2:
            c1 = col1
            while c1 <= c2:
                self.rectangle[r1][c1] = newValue
                c1 += 1
            r1 += 1

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
