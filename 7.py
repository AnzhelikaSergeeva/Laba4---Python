import Deque

with open('files/7.txt', 'r') as file:

    general_stack = Deque.Deque()

    positive_numbers_stack = Deque.Deque()
    negative_numbers_stack = Deque.Deque()

    for line in file:
        text_string = line[:-1].split(' ')

        for number in text_string:
            general_stack.add_first(number)

    for i in range(general_stack.size()):
        cur_number = general_stack.remove_first()

        if int(cur_number) >= 0:
            positive_numbers_stack.add_first(cur_number)
        else:
            negative_numbers_stack.add_first(cur_number)

    positive_numbers_string = ""
    for i in range(positive_numbers_stack.size()):
        positive_numbers_string += positive_numbers_stack.remove_first()
        positive_numbers_string += " "
    print(positive_numbers_string)

    negative_numbers_string = ""
    for i in range(negative_numbers_stack.size()):
        negative_numbers_string += negative_numbers_stack.remove_first()
        negative_numbers_string += " "
    print(negative_numbers_string)