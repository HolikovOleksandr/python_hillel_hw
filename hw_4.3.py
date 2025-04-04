import random


lst = [random.randint(0, 9) for _ in range(random.randint(3, 10))]
print("Початковий список:", lst)

result = [lst[0], lst[2], lst[-2]]
print("Результат:", result)
