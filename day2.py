from input import get_input

input = get_input(2)
for i in range(len(input)):
    input[i] = [ int(level) for level in input[i].split(' ')]

def _is_incremental(report: list[int]) -> bool:
    if report[0] == report[1]:
        return False 
    increasing = True if report[0] < report[1] else False
    for i in range(1, len(report) - 1):
        if (increasing and report[i] >= report[i+1]) \
            or (not increasing and report[i] <= report[i+1]):
            return False
    return True

def _check_levels(report: list[int]) -> bool:
    return all(
        abs(report[i] - report[i+1]) <= 3
        for i in range(len(report) - 1)
    )

def _is_safe(report: list[int]) -> bool:
    return _is_incremental(report) and _check_levels(report)

def _is_problem_dampener(report: list[int]) -> bool:
    return any(
        _is_safe(report[:i] + report[i+1:])
        for i in range(len(report))
    )

def part_one():
    safe = sum(1 for report in input if _is_safe(report))
    print(f'part one: {safe}')

def part_two():
    safe = sum(
        1
        for report in input if _is_safe(report) or _is_problem_dampener(report)
    )
    print(f'part two: {safe}')

if __name__ == '__main__':
    part_one()
    part_two()
