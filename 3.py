import Stack


def move(tower_from, tower_to):
    cur_disk = None
    if tower_from == 'A':
        cur_disk = tower1.pop()
    elif tower_from == 'B':
        cur_disk = tower2.pop()
    else:
        cur_disk = tower3.pop()

    if tower_to == 'A':
        tower1.push(cur_disk)
    elif tower_to == 'B':
        tower2.push(cur_disk)
    else:
        tower3.push(cur_disk)

    print("Move one disk from tower \"{}\" to tower \"{}\"".format(tower_from, tower_to))
    tower1.print_stack()
    tower2.print_stack()
    tower3.print_stack()


def move_tower(disks_amount, tower1, tower2, temp_tower):
    if disks_amount == 0:
        return

    move_tower(disks_amount - 1, tower1, temp_tower, tower2)
    move(tower1, tower2)
    move_tower(disks_amount - 1, temp_tower, tower2, tower1)


tower1 = Stack.Stack()
tower2 = Stack.Stack()
tower3 = Stack.Stack()

for disk in range(int(input("Enter the amount of disks on the first tower ")), 0, -1):
    tower1.push(disk)

move_tower(tower1.size(), 'A', 'C', 'B')