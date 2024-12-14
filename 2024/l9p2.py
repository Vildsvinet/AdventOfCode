# Advent of Code, 2024, day 9

debug_mode = False

# linked list: chunk is node
class Node:
    def __init__(self, ID: int, start: int, size: int, prev, next=None):
        self.ID = ID # -1 for empty
        self.start = start # start index of the chunk
        self.size = size # length of the chunk
        self.prev = prev # chunk left of this chunk
        self.next = next # chunk right of this chunk
        self.is_moved = False

    def set_next (self, node):
        self.next = node

    def set_size(self, size):
        self.size = size

    def set_moved (self):
        self.is_moved = True

    # def __str__(self):
    #     return f'ID: {self.ID} range:{self.start, self.start + self.size}'
    def __str__(self):
        if self.ID == -1: return ' .'*self.size
        else: return f"{self.ID:2}"*self.size

def debug(s: str):
    global debug_mode
    if debug_mode:
        print(s)

even = lambda x: x % 2 == 0
odd = lambda x: not even(x)
def calc_memory_size(diskmap: str) -> int:
    return sum(int(c) for c in diskmap)


def initialise_ll(diskmap: str):
    current_memory_size = 0

    first_ptr = None
    current_ptr = None

    first_ptr = Node(ID=0, start=0, size=int(diskmap[0]), prev=None)
    current_memory_size += int(diskmap[0])

    current_ptr = first_ptr

    for pos, c in enumerate(diskmap[1::]):
        digit=int(c)
        if odd(pos): # occupied
            current = Node(ID=(pos // 2)+1, start=current_memory_size, size = digit, prev=current_ptr)
        else:  # empty
            current = Node(ID=-1, start=current_memory_size, size=digit, prev=current_ptr)

        current_ptr.set_next(current)
        current_ptr = current
        current_memory_size += digit

    last_ptr = current_ptr

    return first_ptr, last_ptr


def print_ll (first: Node):
    global debug_mode
    if debug_mode:
        node = first
        while node:
            print(node, end='')
            node = node.next
        print()

def print_ll_always (first: Node):
    node = first
    i = 0
    while node and i <200:
        print(node, end='')
        node = node.next
        i += 1
    print()

def find_tail(head: Node):
    curr = head
    while curr.next:
        curr=curr.next
    return curr

def find_last_occupied(last: Node):
    # node is empty if ID = -1
    node = last
    while node:
        # print(node)
        if node.ID != -1 and not node.is_moved:
            # print(node.ID)
            return node
        node = node.prev
    return None

def find_first_free(first: Node, candidate: Node):
    node = first
    while node != candidate:
        if node.ID == -1 and node.size >= candidate.size:
            return node
        node = node.next
    return None # no available space


def remove_file(current: Node):
    new_blank = Node(ID=-1, start= current.start, size=current.size, prev=current.prev, next=current.next)

    # if free space to the right:
    if new_blank.next and new_blank.next.ID == -1:
        new_blank.set_size(new_blank.size + new_blank.next.size)
        new_blank.set_next(new_blank.next.next)

    # if free space to the left:
    if new_blank.prev and new_blank.prev.ID == -1:
        new_blank.set_size(new_blank.size + new_blank.prev.size)
        new_blank.start = new_blank.prev.start
        # current.prev.prev.set_next(new_blank)
        new_blank.prev = current.prev.prev

    new_blank.prev.next = new_blank
    if new_blank.next:
        new_blank.next.prev = new_blank

    return new_blank

def insert_file(spot: Node, current: Node):
    before = spot.prev
    after = spot.next

    # move and adjust left side:
    current.start = spot.start
    current.prev = spot.prev
    before.next = current

    # fill the entire space:
    if spot.size == current.size:
        current.next = after
        after.prev = current

    # fill parts of the space
    elif current.size < spot.size:
        spot.start = current.start + current.size
        spot.size = spot.size - current.size
        spot.prev = current
        current.next = spot

    else: print ("wtf???")
    if current.next.ID == current.ID:
        print("Something is about to get ugly", current.ID)


def move_fileblock(first, last) :
    # find candidate:
    candidate = find_last_occupied(last)
    if not candidate:
        return 0, None # evertyhing is either moved or cannot be moved

    # need to find candidate.size free space
    free_spot = find_first_free(first, candidate)
    if not free_spot: # not enough available space
        candidate.is_moved = True # only attempt once
        return 1, last

    # where the file was before will now be free space
    new = remove_file(candidate)
    if not new.next:
        last = new

    insert_file(free_spot, candidate)
    candidate.is_moved = True

    return 2, last


def checksum_node(node: Node) -> int:
    count = 0
    for i in range(node.size):
        count += node.ID * (node.start + i)
    return count

def calc_checksum(first: Node) -> int:
    count = 0
    node = first
    while node.next:
        if node.ID != -1:
            count += checksum_node(node)
        node = node.next
    return count

def main():
    with open("i9_ex.txt", 'r') as inp:
        input = inp.read()

        first, last = initialise_ll(input)
        print_ll(first)

        move_fileblock(first, last)
        print_ll(first)
        last = find_tail(first)

        outcome, lst = 3, last
        while outcome != 0:
            outcome, lst = move_fileblock(first, lst)
            # continue
            print_ll(first)

        print("Just checksum left")
        # print_ll_always(first)

        print("\nres: ", calc_checksum(first))

main()
