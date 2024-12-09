from itertools import product
from input import get_input

equations = get_input(7)

def _is_equation_true(equation: str, operations: str) -> tuple:
    result, operands = equation.split(': ')
    result = int(result)
    operands = [int(operand) for operand in operands.split(' ')]
    num_operations = len(operands) - 1
    combos = [''.join(p) for p in product(operations, repeat=num_operations)]
    for combo in combos:
        temp_result = operands[0]
        operands_index = 1
        for operand in combo:
            curr_operand = operands[operands_index]
            if operand == '+':
                temp_result += curr_operand
            elif operand == '*':
                temp_result *= curr_operand
            elif operand == '|':
                temp_result = int(str(temp_result) + str(curr_operand))
            operands_index += 1
        if temp_result == result:
            return True, result
    return False, 0

def _get_calibration_result(operations: str) -> int:
    calibration_result = 0
    for equation in equations:
        is_equation_true, result = _is_equation_true(equation, operations)
        if is_equation_true:
            calibration_result += result
    return calibration_result

def part_one():
    print(f'part one: {_get_calibration_result('+*')}')

def part_two():
    print(f'part two: {_get_calibration_result('+*|')}')

if __name__ == '__main__':
    part_one()
    part_two()
