import random

def find_largest_number():
    numbers = []

    while len(numbers) < 10:
        random_num = random.randint(1, 100)
        numbers.append(random_num)

    print(f"Згенерований список: {numbers}")

    max_number = numbers[0]
    index = 1

    while index < len(numbers):
        if numbers[index] > max_number:
            # Якщо знайшли число більше за поточний максимум — оновлюємо його
            max_number = numbers[index]
        index += 1

    print(f"Найбільше число у списку: {max_number}")

if __name__ == "__main__":
    find_largest_number()