# Advent of Code, 2024, day 9

# dict: block is key, file id is value
# empty: .

even = lambda x: x % 2 == 0
odd = lambda x: not even(x)


# post: initial memory layout block by block in a dict
def initialize_dict(diskmap: str) -> dict:
    indiv_blocks: dict = dict()
    blocks = 0

    for pos, c in enumerate(diskmap):
        digit = int(c)
        if even(pos):
            for _ in range(digit):
                indiv_blocks[blocks] = pos // 2  # file ID
                blocks += 1
        else:
            for _ in range(digit):
                indiv_blocks[blocks] = '.'
                blocks += 1

    return indiv_blocks


def calc_memory_size(diskmap: str) -> int:
    return sum(int(c) for c in diskmap)


def find_last_occupied(block_contents: dict) -> int:
    for block in reversed(block_contents.keys()):
        if block_contents[block] != '.':
            # print("last occ: ", block_contents.values())
            return block


def move_fileblocks(block_contents: dict) -> dict:
    last_occupied = len(block_contents) - 1
    for block in block_contents:
        last_occupied = find_last_occupied(block_contents)
        if block_contents[block] == '.' and last_occupied > block:
            # print(block_contents.values())
            block_contents[block] = block_contents[last_occupied]
            block_contents[last_occupied] = '.'


def calc_checksum(block_contents: dict) -> int:
    count = 0
    for block in block_contents:
        if block_contents[block] == '.':
            return count
        count += block * block_contents[block]
    return count


def main():
    with open("i9_ex.txt", 'r') as inp:
        input = inp.read()

        block_contents = initialize_dict(input)
        # print(block_contents)
        move_fileblocks(block_contents)
        # print(str(block_contents.values()))
        print(calc_checksum(block_contents))

main()
