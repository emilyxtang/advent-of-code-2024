from input import get_input

input = get_input(1)

# determine the left and right lists from the input
left_list, right_list = [], []
for line in input:
    line_split = line.split(' ')
    left_list.append(int(line_split[0]))
    right_list.append(int(line_split[-1]))

def part_one():
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)
    distance = 0
    for i in range(len(sorted_left_list)):
        distance += abs(sorted_left_list[i] - sorted_right_list[i])
    print(f'part one: {distance}')

def part_two():
    similarity_score = 0
    for i in range(len(left_list)):
        num = left_list[i]
        similarity_score += num * right_list.count(num)
    print(f'part two: {similarity_score}')

if __name__ == '__main__':
    part_one()
    part_two()
