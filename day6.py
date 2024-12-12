from copy import deepcopy
from functools import lru_cache
from input import get_input

input = [list(line) for line in get_input(6)]
num_rows, num_cols = len(input), len(input[0])

directions = ['^', '>', 'v', '<']

@lru_cache(maxsize=None)
def _get_start_pos() -> tuple:
    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] == directions[0]:
                return row, col

@lru_cache(maxsize=None)
def _in_map(curr_pos: tuple) -> bool:
    return (curr_pos[0] >= 0 and curr_pos[0] < len(input)) \
        and (curr_pos[1] >= 0 and curr_pos[1] < len(input[0]))

@lru_cache(maxsize=None)
def _turn_right(direction: str) -> str:
    return directions[(directions.index(direction) + 1) % len(directions)]

def _is_obstacle(map: list[list[str]], next_pos: tuple, 
                 obstruction: tuple=None) -> bool:
    if (map[next_pos[0]][next_pos[1]] == '#' or map[next_pos[0]][next_pos[1]] == 'O') \
        or (obstruction and next_pos[0] == obstruction[0] \
            and next_pos[1] == obstruction[1]):
        return True
    return False

def _follow_steps(map: list[str], curr_dir: str, curr_pos: tuple,
                  next_pos: tuple, obstruction: tuple=None) -> tuple:
    # check if there is an obstacle in front
    if _is_obstacle(map, next_pos, obstruction):
        curr_dir = _turn_right(curr_dir)
    else:
        map[next_pos[0]][next_pos[1]] = 'X' # mark spot as visited
        curr_pos = next_pos
    return map, curr_dir, curr_pos

@lru_cache(maxsize=None)
def _get_obstructions() -> list[tuple]:
    obstructions = []
    for row in range(num_rows):
        for col in range(num_cols):
            if input[row][col] == '.':
                obstructions.append((row, col))
    return obstructions

@lru_cache(maxsize=None)
def _get_next_pos(dir: str, curr_pos: tuple) -> tuple:
    if dir == '^':
        return curr_pos[0] - 1, curr_pos[1]
    elif dir == '>':
        return curr_pos[0], curr_pos[1] + 1
    elif dir == 'v':
        return curr_pos[0] + 1, curr_pos[1]
    elif dir == '<':
        return curr_pos[0], curr_pos[1] - 1

def part_one() -> None:
    puzzle_map = deepcopy(input)

    curr_dir = '^'
    curr_pos = _get_start_pos()
    next_pos = _get_next_pos(curr_dir, curr_pos)

    while _in_map(next_pos):
        puzzle_map, curr_dir, curr_pos = _follow_steps(
            puzzle_map,
            curr_dir,
            curr_pos,
            next_pos
        )
        next_pos = _get_next_pos(curr_dir, curr_pos)

    pos_visited = sum(''.join(line).count('X') for line in puzzle_map)
    print(f'part one: {pos_visited}')

def part_two():
    obstructions = _get_obstructions()
    num_loops = 0
    for obstruction in obstructions:
        curr_dir = '^'
        curr_pos = _get_start_pos()
        next_pos = _get_next_pos(curr_dir, curr_pos)
        puzzle_map = deepcopy(input)
        puzzle_map[obstruction[0]][obstruction[1]] = 'O'
        loop_not_found = True
        visited = [(curr_dir, curr_pos[0], curr_pos[1])]
        while _in_map(next_pos) and loop_not_found:
            puzzle_map, curr_dir, curr_pos = _follow_steps(
                puzzle_map,
                curr_dir,
                curr_pos,
                next_pos,
                obstruction
            )
            next_pos = _get_next_pos(curr_dir, curr_pos)
            if (curr_dir, curr_pos[0], curr_pos[1]) in visited:
                loop_not_found = False
                num_loops += 1
            else:
                visited.append((curr_dir, curr_pos[0], curr_pos[1]))
    print(f'part two: {num_loops}')

if __name__ == '__main__':
    part_one()
    part_two()
