from collections import defaultdict, deque
from input import get_input

input = get_input(5)
rules_input = True
rules, updates = {}, []
for i in range(len(input)):
    line = input[i]
    if not line:
        rules_input = False
        continue
    if rules_input:
        before, after = line.split('|')
        if before in rules:
            rules[before].append(after)
        else:
            rules[before] = [after]
    else:
        updates.append(line)

incorrect_update_pages = []

def _is_after(before: int, after: int) -> bool:
    return before in rules and after in rules[before]

def _is_correct_order(pages: list[str]) -> bool:
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if not _is_after(pages[i], pages[j]):
                return False
    return True

def _build_graph(pages: list[str]) -> tuple[dict[str, list[str]], dict[str, int]]:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # only consider rules for the given pages
    for before, after_list in rules.items():
        if before not in pages:
            continue
        for after in after_list:
            if after in pages:
                graph[before].append(after)
                in_degree[after] += 1

    # ensure all pages are represented in the in-degree dict
    for page in pages:
        if page not in in_degree:
            in_degree[page] = 0

    return graph, in_degree

def _reorder_pages(pages: list[str]) -> list[str]:
    graph, in_degree = _build_graph(pages)

    # topological sort using a queue
    queue = deque([node for node in pages if in_degree[node] == 0])
    ordered_pages = []

    while queue:
        current = queue.popleft()
        ordered_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_pages

def part_one():
    middle_page_nums = 0
    for update in updates:
        pages = update.split(',')
        if _is_correct_order(pages):
            middle_page_nums += int(pages[len(pages) // 2])
        else:
            incorrect_update_pages.append(pages)
    print(f'part one: {middle_page_nums}')

def part_two():
    middle_page_nums = 0
    for incorrect_pages in incorrect_update_pages:
        correct_pages = _reorder_pages(incorrect_pages)
        middle_page_nums += int(correct_pages[len(correct_pages) // 2])
    print(f'part two: {middle_page_nums}')

if __name__ == '__main__':
    part_one()
    part_two()
