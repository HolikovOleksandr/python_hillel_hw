four_digit_number = int(input("Plese, enter a 4-digit number: "))

first_digit = four_digit_number // 1000
second_digit = (four_digit_number // 100) % 10
third_digit = (four_digit_number // 10) % 10
fourth_digit = four_digit_number % 10

print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)