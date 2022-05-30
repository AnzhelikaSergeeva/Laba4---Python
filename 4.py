import Stack

with open('files/4-5.txt', 'r') as file:

    for line in file:
        text_string = line[:-1]

        balance = Stack.Stack()
        balance_broken = False

        for i in text_string:
            if i == "(":
                balance.push(i)
            elif i == ")":
                cur_symbol = balance.pop()
                if cur_symbol is None:
                    balance_broken = True
                    break

        if balance.size() != 0:
            balance_broken = True
            break

    if balance_broken:
        print("Balance is broken")
    else:
        print("Balance is fine")