from typing import List, Tuple
from enum import Enum, auto


def read_inputs():
    global _word_search
    _word_search = []
    f = open("input", "r")
    for line in f:
        row = []
        for char in line:
            if char == "\n":
                continue
            row.append(char)
        _word_search.append(row)
    f.close()
    global _row_bound
    _row_bound = len(_word_search)-1
    global _col_bound
    _col_bound = len(_word_search[0])-1


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    UPPERLEFT = auto()
    UPPERRIGHT = auto()
    LOWERLEFT = auto()
    LOWERRIGHT = auto()

    def move(self) -> Tuple[int, int]:
        if self == Direction.UP:
            return (-1, 0)
        elif self == Direction.DOWN:
            return (1, 0)
        elif self == Direction.LEFT:
            return (0, -1)
        elif self == Direction.RIGHT:
            return (0, 1)
        elif self == Direction.UPPERLEFT:
            return (-1, -1)
        elif self == Direction.UPPERRIGHT:
            return (-1, 1)
        elif self == Direction.LOWERLEFT:
            return (1, -1)
        elif self == Direction.LOWERRIGHT:
            return (1, 1)


def recursive_search(letter: str, position: Tuple[int, int], direction: Direction) -> int:
    r, c = position
    if r < 0 or r > _row_bound or c < 0 or c > _col_bound:
        return 0
    # Calculate movement
    x, y = direction.move()
    move_pos = (r + x, c + y)
    # check that letter matches what we are looking for
    if _word_search[r][c] == letter:
        if letter == "M":
            return recursive_search("A", move_pos, direction)
        elif letter == "A":
            return recursive_search("S", move_pos, direction)
        elif letter == "S":
            return 1
    # if letter does not match, return 0
    else:
        return 0


def count_xmas() -> int:
    xmas_count = 0
    for r_idx, row in enumerate(_word_search):
        for c_idx, letter in enumerate(row):
            if letter == "X":
                # UP
                up = Direction.UP.move()
                up_pos = (r_idx + up[0], c_idx + up[1])
                # DOWN
                down = Direction.DOWN.move()
                down_pos = (r_idx + down[0], c_idx + down[1])
                # LEFT
                left = Direction.LEFT.move()
                left_pos = (r_idx + left[0], c_idx + left[1])
                # RIGHT
                right = Direction.RIGHT.move()
                right_pos = (r_idx + right[0], c_idx + right[1])
                # UPPERLEFT
                upperleft = Direction.UPPERLEFT.move()
                upperleft_pos = (r_idx + upperleft[0], c_idx + upperleft[1])
                # UPPERRIGHT
                upperright = Direction.UPPERRIGHT.move()
                upperright_pos = (r_idx + upperright[0], c_idx + upperright[1])
                # LOWERLEFT
                lowerleft = Direction.LOWERLEFT.move()
                lowerleft_pos = (r_idx + lowerleft[0], c_idx + lowerleft[1])
                # LOWERRIGHT
                lowerright = Direction.LOWERRIGHT.move()
                lowerright_pos = (r_idx + lowerright[0], c_idx + lowerright[1])
                # Search in all directions and add to xmas count
                xmas_count += recursive_search("M", up_pos, Direction.UP)
                xmas_count += recursive_search("M", down_pos, Direction.DOWN)
                xmas_count += recursive_search("M", left_pos, Direction.LEFT)
                xmas_count += recursive_search("M", right_pos, Direction.RIGHT)
                xmas_count += recursive_search("M", upperleft_pos, Direction.UPPERLEFT)  # noqa
                xmas_count += recursive_search("M", upperright_pos, Direction.UPPERRIGHT)  # noqa
                xmas_count += recursive_search("M", lowerleft_pos, Direction.LOWERLEFT)  # noqa
                xmas_count += recursive_search("M", lowerright_pos, Direction.LOWERRIGHT)  # noqa

    return xmas_count

def count_x_mas() -> int:
    xmas_count = 0
    for r_idx, row in enumerate(_word_search):
        for c_idx, letter in enumerate(row):
            # skip the coordinates of MAS's that have already been found - make sure to not skip them when checking for the second MAS
            if letter == "M":
                # UPPERRIGHT
                upperright = Direction.UPPERRIGHT.move()
                upperright_pos = (r_idx + upperright[0], c_idx + upperright[1])
                # LOWERLEFT
                lowerleft = Direction.LOWERLEFT.move()
                lowerleft_pos = (r_idx + lowerleft[0], c_idx + lowerleft[1])
                # LOWERRIGHT
                lowerright = Direction.LOWERRIGHT.move()
                lowerright_pos = (r_idx + lowerright[0], c_idx + lowerright[1])
                # Search in diagonal directions and add to xmas count
                # If MAS is found then we need to find the matching diagonal MAS that completes the X (make sure to add the position of the second found MAS to the skip_list)
                # Don't check UPPERLEFT direction because other cases will cover these
                if recursive_search("A", upperright_pos, Direction.UPPERRIGHT):  # noqa
                    # UPPERRIGHT: don't check two spaces up because this cross will have been found already; check two spaces right
                    if recursive_search("M", (r_idx, c_idx+2), Direction.UPPERLEFT):
                        xmas_count += 1
                if recursive_search("A", lowerleft_pos, Direction.LOWERLEFT):  # noqa
                    # LOWERLEFT: don't check two spaces left because this cross will have been found already; check two spaces down
                    if recursive_search("M", (r_idx+2, c_idx), Direction.UPPERLEFT):
                        xmas_count += 1
                if recursive_search("A", lowerright_pos, Direction.LOWERRIGHT):  # noqa
                    # LOWERRIGHT: check two spaces down and two spaces right
                    if recursive_search("M", (r_idx+2, c_idx), Direction.UPPERRIGHT):
                        xmas_count += 1
                    if recursive_search("M", (r_idx, c_idx+2), Direction.LOWERLEFT):
                        xmas_count += 1

    return xmas_count


if __name__ == "__main__":
    read_inputs()
    part1_xmas_count = count_xmas()
    part2_xmas_count = count_x_mas()
    print(f'Part1: {part1_xmas_count}')
    print(f'Part2: {part2_xmas_count}')
