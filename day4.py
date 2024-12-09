from input import get_input

word_search = get_input(4)
num_rows, num_cols = len(word_search), len(word_search[0])

def _get_all_diagonals(len_find_str: int) -> list[str]:
    diagonals = []

    for d in range(num_rows + num_cols - 1):
        major_diagonal = [] # top-left to bottom-right
        minor_diagonal = [] # top-right to bottom-left

        for row in range(max(0, d - num_cols + 1), min(num_rows, d + 1)):
            col_major = d - row
            col_minor = num_cols - 1 - (d - row)

            major_diagonal.append(word_search[row][col_major])
            minor_diagonal.append(word_search[row][col_minor])

        if len(major_diagonal) >= len_find_str:
            diagonals.append(''.join(major_diagonal))
        if len(minor_diagonal) >= len_find_str:
            diagonals.append(''.join(minor_diagonal))

    return diagonals

def _is_x(row: int, col: int) -> bool:
    if (row - 1 >= 0 and row + 1 < num_rows) \
        and (col - 1 >= 0 and col + 1 < num_cols):
        diagonal1 = word_search[row - 1][col - 1] + 'A' + word_search[row + 1][col + 1]
        diagonal2 = word_search[row - 1][col + 1] + 'A' + word_search[row + 1][col - 1]
        if (diagonal1 == 'SAM' and diagonal2 == 'SAM') \
            or (diagonal1 == 'SAM' and diagonal2[::-1] == 'SAM') \
            or (diagonal1[::-1] == 'SAM' and diagonal2 == 'SAM') \
            or (diagonal1[::-1] == 'SAM' and diagonal2[::-1] == 'SAM'):
                return True
    return False

def part_one():
    find_str_count = 0
    find_str = 'XMAS'
    find_str_reversed = find_str[::-1]

    # check all horizontals
    for row in word_search:
        find_str_count += row.count(find_str) + row.count(find_str_reversed)

    # check all verticals
    for col in range(num_cols):
        vertical = ''
        for row in range(num_rows):
            vertical += word_search[row][col]
        find_str_count += vertical.count(find_str) + vertical.count(find_str_reversed)

    # check all diagonals
    for diagonal in _get_all_diagonals(len(find_str)):
        find_str_count += diagonal.count(find_str) + diagonal.count(find_str_reversed)

    print(f'part one: {find_str_count}')

def part_two():
    x_count = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if word_search[row][col] == 'A' and _is_x(row, col):
                x_count += 1
    print(f'part two: {x_count}')

if __name__ == '__main__':
    part_one()
    part_two()
