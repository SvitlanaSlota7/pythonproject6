import random

def exclusive_common_numbers():
    list1 = []
    list2 = []

    while len(list1) < 10:
        list1.append(random.randint(1, 10))
        list2.append(random.randint(1, 10))

    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")

    #  спільні числа двох списків без дублікатів
    common_list = []
    i = 0

    while i < len(list1):
        number = list1[i]

        # перевірка на дублікати
        if number in list2 and number not in common_list:
            common_list.append(number)

        i += 1

    print(f"Спільні числа: {common_list}")

if __name__ == "__main__":
    exclusive_common_numbers()