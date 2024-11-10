def process_string(input_string):
    S1 = {input_string[i] for i in range(0, len(input_string), 2)}  
    S2 = {input_string[i] for i in range(1, len(input_string), 2)} 

    print(f"S1 (парні позиції): {S1}")
    print(f"S2 (непарні позиції): {S2}")

    if S1.issubset(S2):
        result = S2 - S1
        print(f"Різниця множин S2 - S1: {result}")
    else:
        result = S1 | S2
        print(f"Об'єднання множин S1 і S2: {result}")

input_string = "abcdefg"
process_string(input_string)
