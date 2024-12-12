from typing import List, Tuple


def print_map(lab_map: List[List[str]]):
    for row in lab_map:
        for char in row:
            print(char, end="")
        print()


def read_inputs() -> Tuple[List[List[str]], Tuple[str, int, int]]:
    lab_map = []
    f = open("input", "r")
    guard_pos = ("", -1, -1)
    for r, line in enumerate(f):
        if line[-1] == "\n":
            line = line[:-1]
        row = []
        for c, char in enumerate(line):
            row.append(char)
            if char == "^" or char == "<" or char == ">" or char == "v":
                guard_pos = (char, r, c)
        lab_map.append(row)
    f.close()
    return (lab_map, guard_pos)


def in_bounds(position: Tuple[int, int], bounds: Tuple[int, int]) -> bool:
    row_bound, col_bound = bounds
    if position[0] >= 0 and position[0] < row_bound and position[1] >= 0 and position[1] < col_bound:
        return True
    return False


def get_movement(direction: str, position: Tuple[int, int]) -> Tuple[int, int]:
    if direction == "^":
        return (position[0]-1, position[1])
    elif direction == "<":
        return (position[0], position[1]-1)
    elif direction == ">":
        return (position[0], position[1]+1)
    elif direction == "v":
        return (position[0]+1, position[1])


def turn_right(direction: str) -> str:
    if direction == "^":
        return ">"
    elif direction == "<":
        return "^"
    elif direction == ">":
        return "v"
    elif direction == "v":
        return "<"


def predict_guard_movement(lab_map: List[List[str]], guard_pos: Tuple[str, int, int]) -> int:
    distinct_spaces = 1
    direction = guard_pos[0]
    position = (guard_pos[1], guard_pos[2])
    row_bound = len(lab_map)
    col_bound = len(lab_map[0])
    while position[0] >= 0 and position[0] < row_bound and position[1] >= 0 and position[1] < col_bound:
        # print("================================================")
        # print_map(lab_map)
        # check next move to determine what to do
        next_space = get_movement(direction, position)
        if in_bounds(next_space, (row_bound, col_bound)):
            # Obstacle
            if lab_map[next_space[0]][next_space[1]] == "#":
                direction = turn_right(direction)
                lab_map[position[0]][position[1]] = direction
            # No obstacle, move one space and add to count
            else:
                if lab_map[next_space[0]][next_space[1]] == ".":
                    distinct_spaces += 1
                lab_map[position[0]][position[1]] = "X"
                position = next_space
                lab_map[position[0]][position[1]] = direction
                    
        else:
            # guard jumped off the map, report distinct spaces
            break
    
    return distinct_spaces

if __name__ == "__main__":
    lab_map, guard_pos = read_inputs()
    # print("Predicting Guard Movement...")
    distinct_spaces = predict_guard_movement(lab_map, guard_pos)
    print(f'Part1: {distinct_spaces}')