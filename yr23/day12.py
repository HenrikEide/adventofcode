import sys

# springs = [x.split() for x in sys.stdin.readlines()]

def sep(row: str) -> str:
    return row.replace('?', '.',1)

def count_combinations(row, blocks, index=0):
    if not blocks:
        return int(all(x in {'.', '#'} for x in row[index:]))
    block_size = blocks[0]
    combinations = 0
    for i in range(index, len(row)):
        if all(x in {'?', '#'} for x in row[i:i + block_size]) and (i + block_size == len(row) or row[i + block_size] == '.'):
            new_row = row[:i] + '#' * block_size + sep(row[i + block_size:])
            combinations += count_combinations(new_row, blocks[1:], i + block_size + 1)
        if i < len(row) and row[i] == '#':
            break
    return combinations

springs = [x.split() for x in [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1"
    ]]
for row, ns in springs:
    ns = [int(x) for x in ns.split(",")]
    print(count_combinations(row, ns))
