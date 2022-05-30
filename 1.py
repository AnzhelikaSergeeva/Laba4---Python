import Deque

deque = Deque.Deque()
res_deque = Deque.Deque()
with open('files/1.txt', 'r') as file:
    # Filling the deque with content from file
    for line in file:
        deque.add_last(line[:-1])

    for i in range(deque.size()-1):
        for j in range(deque.size()):
            el1 = deque.remove_first()
            el2 = deque.remove_last()
            if el1 > el2:
                deque.add_last(el1)
                deque.add_last(el2)
            else:
                deque.add_last(el2)
                deque.add_last(el1)
        res_deque.add_last(deque.remove_last())
    res_deque.add_last(deque.remove_last())

    for i in range(res_deque.size()):
        print("{}) {}".format(i+1, res_deque.remove_first()))