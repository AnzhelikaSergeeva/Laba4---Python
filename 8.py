import Stack

with open('files/8.txt', 'r') as file:

    general_stack = Stack.Stack()

    for line in file:
        text_string = line[:-1].split(' ')

        for word in text_string:
            general_stack.push(word)

    string = ''
    for i in range(general_stack.size()):
        string += general_stack.pop()
        string += ' '

    with open('files/8-test.txt', 'w') as f:
        f.write(string)