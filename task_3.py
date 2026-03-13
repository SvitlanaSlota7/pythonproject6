def extract_numbers():

    all_numbers = []
    num = 1
    while num <= 100:
        all_numbers.append(num)
        num += 1

    # знаходимо числа, що діляться на 7, але не кратні 5
    filtered_numbers = []
    index = 0

    #  ітерація по створеному списку
    while index < len(all_numbers):
        current = all_numbers[index]

           # current % 7 == 0  -> ділиться на 7 без залишку
        # current % 5 != 0  -> не ділиться на 5 без залишку
        if current % 7 == 0 and current % 5 != 0:
            filtered_numbers.append(current)

        index += 1

    print("Числа від 1 до 100, що діляться на 7, але не на 5:")
    print(filtered_numbers)


if __name__ == "__main__":
    extract_numbers()