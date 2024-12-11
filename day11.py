from functools import lru_cache
from input import get_input

input = get_input(11)[0]

@lru_cache(maxsize=None)
def _get_num_stones(stone: int, depth: int) -> int:
    if depth == 0:
        return 1

    depth -= 1

    if stone == 0:
        return _get_num_stones(1, depth)
    
    stone_str = str(stone)
    stone_len = len(stone_str)
    if stone_len % 2 == 0:
        midpoint = stone_len // 2
        left = int(stone_str[:midpoint])
        right = int(stone_str[midpoint:])
        return _get_num_stones(left, depth) + _get_num_stones(right, depth)
    
    return _get_num_stones(stone * 2024, depth)
    
def _get_num_stones_after_blinks(blinks: int) -> int:
    stones = [int(stone) for stone in input.split(' ')]
    return sum(_get_num_stones(stone, blinks) for stone in stones)

def part_one():
    print(f'part one: {_get_num_stones_after_blinks(25)}')

def part_two():
    print(f'part two: {_get_num_stones_after_blinks(75)}')

if __name__ == '__main__':
    part_one()
    part_two()
