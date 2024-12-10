import re
from typing import Tuple

def read_inputs() -> str:
    input_str = ""
    f = open("input", "r")
    for line in f:
        if line[-1] == "\n":
            input_str += line[:-1]
        else:
            input_str += line
    f.close()
    return input_str

def scan_corrupt_mem(corrupt_mem: str) -> Tuple[int, int]:
    part1_result = 0
    part2_result = 0
    # result = 0
    valid_instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', corrupt_mem)
    execute = True
    for instr in valid_instructions:
        if instr == "do()":
            execute = True
        elif instr == "don't()":
            execute = False
        else:
            nums = instr[4:-1].split(",")
            prod = int(nums[0]) * int(nums[1])
            part1_result += prod
            if execute:
                nums = instr[4:-1].split(",")
                prod = int(nums[0]) * int(nums[1])
                part2_result += prod
    return part1_result, part2_result

if __name__ == "__main__":
    corrupt_mem = read_inputs()
    part1_result, part2_result = scan_corrupt_mem(corrupt_mem)
    print(f'Part1: {part1_result}\nPart2: {part2_result}')
    