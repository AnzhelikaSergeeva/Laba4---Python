import Deque

text = Deque.Deque()
key = Deque.Deque()
decoded_text = Deque.Deque()

alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    key.add_last(i)


with open('files/2.txt', 'r') as file:
    for line in file:
        text_string = line[:-1]
        for i in text_string:
            text.add_last(i)

        for i in range(text.size()):
            text_symbol = text.remove_first()
            if text_symbol in [" ", "'", ",", "?"]:
                decoded_text.add_last(text_symbol)
                continue
            while True:
                key_symbol = key.remove_last()
                if key_symbol != text_symbol:
                    key.add_first(key_symbol)
                else:
                    key.add_first(key_symbol)
                    key_symbol = key.remove_last()
                    key.add_first(key_symbol)
                    decoded_text.add_last(key.get_last())
                    break

        res_string = ""
        for i in range(decoded_text.size()):
            res_string += decoded_text.remove_first()

        print(res_string)