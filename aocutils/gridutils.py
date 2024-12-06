from enum import Enum
from typing import Self
from multipledispatch import dispatch

class Direction(Enum):
    LEFT = (0, -1)
    UPLEFT = (-1, -1)
    UP = (-1, 0)
    UPRIGHT = (-1, 1)
    RIGHT = (0, 1)
    DOWNRIGHT = (1, 1)
    DOWN = (1, 0)
    DOWNLEFT = (1, -1)

    @classmethod
    def turn90Right(cls, d: Self) -> Self:
        return Direction((d.value[1], -d.value[0]))

    @classmethod
    def turn90Left(cls, d: Self) -> Self:
        return Direction((-d.value[1], d.value[0]))

    @classmethod
    def turnAround(cls, d: Self) -> Self:
        return Direction((-d.value[0], -d.value[1]))

class Pos:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
    
    @dispatch(int, int)
    def move(self, dx: int, dy: int) -> Self:
        return Pos(self.x + dx, self.y + dy)
    
    @dispatch(Direction)
    def move(self, d: Direction) -> Self:
        return self.move(d.value[0], d.value[1])
    
    def backtrack(self, d: Direction) -> Self:
        return self.move(-d.value[0], -d.value[1])

class Grid:
    def __init__(self, lines: list[list[str]]):
        self.grid: list[list[str]] = lines
        self.height: int = len(lines)
        self.width: int = len(lines[0])

    def getPos(self, p: Pos):
        return self.grid[p.x][p.y]
    
    @dispatch(int, int)
    def outOfGrid(self, i: int, j: int) -> bool:
        return i < 0 or i > self.height - 1 or j < 0 or j > self.width - 1
    
    @dispatch(Pos)
    def outOfGrid(self, p: Pos) -> bool:
        return self.outOfGrid(p.x, p.y)
    
    def makeCopy(self) -> Self:
        return Grid(self.grid)
    
    def get(self, p: Pos) -> str:
        return self.grid[p.x][p.y]

    def find(self, token: str) -> Pos:
        for idx, g in enumerate(self.grid):
            if token in g:
                return Pos(idx, g.index(token))
        return None

    @dispatch(int, int, str)
    def replace(self, i: int, j: int, val: str) -> None:
        self.grid[i][j] = val
    
    @dispatch(Pos, str)
    def replace(self, p: Pos, val: str) -> None:
        self.replace(p.x, p.y, val)

if __name__ == "__main__":
    print(Direction.turn90Right(Direction.LEFT))
    print(Direction.turn90Left(Direction.LEFT))
    print(Direction.turnAround(Direction.LEFT))