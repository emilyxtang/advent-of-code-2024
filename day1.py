from input import get_input

input = get_input(1)

# determine the left and right lists from the input
left_list, right_list = [], []
for line in input:
    line_split = line.split(' ')
    left_list.append(int(line_split[0]))
    right_list.append(int(line_split[-1]))

def part_one():
    distance = sum(
        abs(left - right)
        for left, right in zip(sorted(left_list), sorted(right_list))
    )
    print(f'part one: {distance}')

def part_two():
    similarity_score = sum(
        num * right_list.count(num)
        for num in left_list
    )
    print(f'part two: {similarity_score}')

if __name__ == '__main__':
    part_one()
    part_two()
