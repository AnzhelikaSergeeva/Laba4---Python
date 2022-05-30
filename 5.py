import Deque

with open('files/4-5.txt', 'r') as file:

    for line in file:
        text_string = line[:-1]

        balance = Deque.Deque()
        balance_broken = False

        for i in text_string:
            if i == "[":
                balance.add_first(i)
            elif i == "]":
                cur_symbol = balance.remove_first()
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